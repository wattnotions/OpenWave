%{
Generates simulated ocean surface displacement data using oceanWaveSim
Converts that displacement data to acceleration using disp2Accel
Then converts this derived accel signal back to displacement using
accel2Disp
%}


num_waves = 30;
fs = 4;
dt=1/fs;
stoptime = 1200; %signal length in seconds
t = (0:dt:stoptime)'; % make time x axis

%generate surface displacement data
original_displacement = oceanWaveSim(num_waves, 0.01, fs, stoptime);

%convert displacement to acceleration
[differentiated_accel, differentiated_velocity] = disp2Accel(original_displacement, t);

%plot fft of original displacement, velocity (disp differentiated once),
%and acceleration(disp differentiated twice)
figure(11)
g = tiledlayout(3,1);

nexttile
multiPlotFFT(fs, length(original_displacement), original_displacement, 'original displacement')

nexttile
multiPlotFFT(fs, length(differentiated_velocity), differentiated_velocity, 'differentiated velocity')

nexttile
multiPlotFFT(fs, length(differentiated_accel), differentiated_accel, 'differentiated accel')

title(g, 'Displacement to acceleration')

%convert acceleration derived above back to displacement
[integrated_disp, integrated_velocity] = accel2Disp(differentiated_accel, t);

%highpass filter the new displacement signal to remove low frequency
%component added due to integration process
integrated_disp = highpass(integrated_disp,0.03, fs,'Steepness',0.96);

%in accel2Disp above we went from the calculated accel signal back to a
%displacement signal. Plot this accel signal, the velocity signal (one
%integration) and the displacement signal (two integrations)
figure(10)
h = tiledlayout(3,1);

nexttile
multiPlotFFT(fs, length(differentiated_accel), differentiated_accel, 'differentiated accel')

nexttile
multiPlotFFT(fs, length(integrated_velocity), integrated_velocity, 'integrated velocity')

nexttile
multiPlotFFT(fs, length(integrated_disp), integrated_disp, 'integrated disp')

title(h, 'Acceleration to displacement')






%plot original displacement signal vs new derived displacement signal
figure(3001)
plot(t,integrated_disp)
hold on
plot(t, original_displacement)
legend('integrated disp', 'original disp')
hold off



