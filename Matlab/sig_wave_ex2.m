


num_waves = 300;
fs = 60;
dt=1/fs;
stoptime = 60;
sample_length = (fs*stoptime)+1;
t = (0:dt:stoptime)'; % seconds 

S = oceanWaveSim(num_waves, 1, fs, stoptime);
plotFFT(fs, sample_length, S);