
fs = 20;

%%% real accel data test
T = readtable('../test_data/rotating_arm_data/20cm_3v.csv');
z_accel = table2array(T(:,3)); %z_accel
t = table2array(T(:,9)); %timestamps
z_accel = lowpass(z_accel,0.15, fs,'Steepness',0.96); %filter out high freq noise

%plot filtered z_accel
figure(2000)
plot(t,z_accel);
title('Z axis acceleration');
xlabel('Time (Seconds)');

z_accel = z_accel - mean(z_accel); %remove dc offset
disp = accel2Disp(z_accel, fs);    %convert accel to displacement
disp = disp-mean(disp);             

%remove low freq noise caused by double integration
disp = highpass(disp,0.15, fs,'Steepness',0.96);
plotFFT(fs, length(disp), disp)

fprintf('Sig wave height = %0.2f\n',sigWaveCalc(disp));

%plot displacement signal
figure(1003)
plot(t,disp);
title('Output displacement')
xlabel('Time (Seconds)')