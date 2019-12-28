num_waves = 30;
fs = 40;
dt=1/fs;
stoptime = 20;
sample_length = (fs*stoptime)+1;

t = (0:dt:stoptime)'; % seconds 

S = oceanWaveSim(num_waves, 1, fs, stoptime);

accel = disp2Accel(S, fs);

disp = accel2Disp(accel, fs);

figure(3)
hold off
plot(t,disp);
hold on
plot(t, S);
legend('Derived displacement','Original Data');
title('Output displacement')
xtitle('Time (Seconds)')