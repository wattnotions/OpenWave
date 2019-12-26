
num_waves = 100;
fs = 10;
dt=1/fs;
stoptime = 40;
sample_length = (fs*stoptime)+1;

t = (0:dt:stoptime)'; % seconds 

S = oceanWaveSim(num_waves, 1, fs, stoptime);
psd_area = psd_test(S, fs);


fprintf('Elevation data signal variance = %0.2f\n',var(S));
fprintf('PSD area under curve = %0.2f\n',psd_area);



figure(4)
plot(t,S);