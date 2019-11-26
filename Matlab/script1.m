m = csvread('..\test_data\20cm_3v.csv');
z_accel = m(:,3);
lp_z = lowpass(z_accel,1,20)     %lowpass filtered z


Fs = 20;            % Sampling frequency in Hz                    
T = 1/Fs;             % Sampling period       
L = length(lp_z);          % Length of signal
t = (0:L-1)*T;        % Time vector

Y=fft(lp_z);

P2 = abs(Y/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);


f = Fs*(0:(L/2))/L;
plot(f,P1) 
title('Single-Sided Amplitude Spectrum of X(t)')
xlabel('f (Hz)')
ylabel('|P1(f)|')