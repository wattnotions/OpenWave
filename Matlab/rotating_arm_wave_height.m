
fs = 20;

%%% real accel data test
T = readtable('20cm_3v.csv');
z_accel = table2array(T(:,3));
t = table2array(T(:,9));
z_accel = lowpass(z_accel,0.15, fs,'Steepness',0.96);
figure(2000)
plot(t,z_accel)

z_accel = z_accel - mean(z_accel);


disp = accel2Disp(z_accel, fs);
disp = disp-mean(disp);
disp = highpass(disp,0.15, fs,'Steepness',0.96);

plotFFT(fs, length(disp), disp)
%%%


disp = highpass(disp,0.1,fs);

%disp = disp - mean(disp);
%plotFFT(fs, length(disp), disp)

fprintf('Sig wave height = %0.2f\n',sigWaveCalc(disp));


figure(1003)
plot(t,disp);
%hold on
%plot(t, S);
%legend('Derived displacement','Original Data');
title('Output displacement')
xlabel('Time (Seconds)')