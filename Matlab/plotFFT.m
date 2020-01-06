%{
1. Takes the FFT of a time domain signal and plots it

Arguments:
Fs            : Sample rate of time domain signal
sample_length : Number of samples in signal
S             : Time domain signal

Example usage: plotFFT(20, 1028, S);
%}

function plotFFT(Fs, sample_length, S);
                
    T = 1/Fs;             % Sampling period       
    L = sample_length;            % Length of signal
    t = (0:L-1)*T;        % Time vector


    Y=fft(S);

    P2 = abs(Y/L);
    P1 = P2(1:floor(L/2+1));
    P1(2:end-1) = 2*P1(2:end-1);

    figure(2)
    f = Fs*(0:(L/2))/L;
    plot(f,P1) 
    grid
    A = trapz(f, P1);
    title('Single-Sided Amplitude Spectrum of X(t)')
    xlabel('f (Hz)')
    ylabel('|P1(f)|')
    
end