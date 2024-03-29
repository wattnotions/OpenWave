%{ 
1.Takes the fft of time domain signal
2. Converts fft to power-spectral-distribution(PSD)
3. Finds the area under the PSD curve

Arguments:
x  : time domain signal
fs : sample rate of signal x
%}

function area = psdArea(x, fs);
    
    rng default
    Fs = fs;
    t = 0:1/Fs:1-1/Fs;
    
    N = length(x);
    xdft = fft(x);
    xdft = xdft(1:floor(N/2+1));
    
    psdx = (1/(Fs*N)) * abs(xdft).^2;
    psdx(2:end-1) = 2*psdx(2:end-1);
    freq = 0:Fs/length(x):Fs/2;
    
    bin_width = fs/N;
    area = sum(psdx)*bin_width;
    
    %{
    figure(11)
    plot(freq,10*log10(psdx))
    grid on
    title('Periodogram Using FFT')
    xlabel('Frequency (Hz)')
    ylabel('Power/Frequency (dB/Hz)')
    %}
    
end