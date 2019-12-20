num_waves = 10000;
fs = 4;
dt=1/fs;
stoptime = 60;
sample_length = (fs*stoptime)+1;


S = oceanWaveSim(num_waves, 1, fs, stoptime);
plotFFT(fs, sample_length, S);


%Plot surface displacement
figure(3)
t = (0:dt:stoptime)'; % seconds 

plot(t,S);
yline((4*std(S))- abs(min(S)));