%{
1. Reads data from a file in the rotating_arm_data folder
2. Gets the acceleration and timestamp values
3. Plots the Z acceleration
4. Converts the Z acceleration to displacement
5. Plots an FFT of the displacement signal
6. Calculates the significant wave height of the disp signal using two
methods, highest 3rd and std dev.
7. Plots the time domain signal
%}


%%% read accel data from csv file
T = readtable('../test_data/rotating_arm_data/40cm_3v.csv');
z_accel = table2array(T(:,3)); %z_accel
timestamps = table2array(T(:,9)); %timestamps
t = formatTimestamp(timestamps); %X axis (milliseconds)
%z_accel = lowpass(z_accel,0.2, fs,'Steepness',0.96); %filter out high freq noise

%plot filtered z_accel
figure(2000)
plot(t,z_accel);
title('Z axis acceleration');
xlabel('Time (Seconds)');

z_accel = z_accel - mean(z_accel); %remove dc offset
disp = accel2Disp(z_accel,t);    %convert accel to displacement
disp = disp-mean(disp);             


%remove low freq noise caused by double integration
disp = highpass(disp,0.1, fs,'Steepness',0.96);
plotFFT(fs, length(disp), disp)

fprintf('Sig wave height (highest 3rd) = %0.2f\n',sigWaveCalc(disp));
fprintf('Sig wave height 4*std = %0.2f\n',4*std(disp));

%plot displacement signal
figure(1003)
plot(t,disp);
title('Output displacement')
xlabel('Time (Seconds)')