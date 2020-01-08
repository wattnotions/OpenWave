%{
1. Takes the FFT of a time domain signal and plots it

Arguments:
Fs            : Sample rate of time domain signal
sample_length : Number of samples in signal
S             : Time domain signal

Example usage: plotFFT(20, 1028, S);
%}

function multiPlotFFT(Fs, sample_length, S,title_name);
                
    T = 1/Fs;             % Sampling period       
    L = sample_length;            % Length of signal
    t = (0:L-1)*T;        % Time vector


    Y=fft(S);

    P2 = abs(Y/L);
    P1 = P2(1:floor(L/2+1));
    P1(2:end-1) = 2*P1(2:end-1);

    f = Fs*(0:(L/2))/L;
    plot(f,P1) 
    grid
    A = trapz(f, P1);
    title(title_name)
    xlabel('f (Hz)')
    ylabel('|P1(f)|')
    xlim([0,0.7])
    
end