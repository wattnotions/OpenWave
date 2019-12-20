num_waves = 10000;
fs = 4;
dt=1/fs;
stoptime = 60;
sample_length = (fs*stoptime)+1;
t = (0:dt:stoptime)'; % seconds 

S = oceanWaveSim(num_waves, 1, fs, stoptime);
%plotFFT(fs, sample_length, S);


sig_wave_height = sigWaveCalc(S);
fprintf('Simulated wave sig wave height (4*std_dev) = %f\n',4*std(S));
fprintf('Simulated wave sig wave height (highest 3rd) = %f\n',sig_wave_height);

yline(sig_wave_height/2,'--g','Hightest 3rd Calc');
yline((4*std(S))/2,'b','4*std Calc');

