%{
Generates simulated ocean elavation data
Calculates significant wave height in the time domain and the freq domain
(Area under PSD curve is equal to variance of time domain signal)
%}


num_waves = 100;
fs = 10;
dt=1/fs;
stoptime = 40;
sample_length = (fs*stoptime)+1;

t = (0:dt:stoptime)'; % seconds 

S = oceanWaveSim(num_waves, 1, fs, stoptime);
psd_area = psdArea(S, fs);


fprintf('Elevation data signal variance = %0.2f\n',var(S));
fprintf('PSD area under curve = %0.2f\n',psd_area);

fprintf('Significant wave height (time domain calc) = %0.2f\n',4*sqrt(var(S)));
fprintf('Significant wave height (freq domain calc) = %0.2f\n',4*sqrt(psd_area));



figure(4)
plot(t,S);
