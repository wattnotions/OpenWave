num_waves = 10; %Number of sine waves to create and add together

%Generate wave amplitudes based on normal distribution
r = normrnd(0,1,[1,num_waves]); %Generate random numbers
amps = r + abs(min(r));        %shift values to positive numbers

%histogram(amps, 100);



%Generate random frequencies between 0.05-0.67Hz
min_freq=0.05;
max_freq=0.67;
n=num_waves;
freqs=min_freq+rand(1,n)*(max_freq-min_freq);

%Generate random phase shifts
min_phase=0;
max_phase=360;
n=num_waves;
phases=min_phase+rand(1,n)*(max_phase-min_phase);



fs = 200;         %sampling frequency in hz
stoptime = 50; %sample length in seconds
num_samples =  (fs*stoptime)+1;

waves = zeros(num_waves, num_samples);  %define matrix to store sine wave vectors in

for i = 1:num_waves 
   waves(i,:) = sineGen(amps(i), freqs(i), phases(i), stoptime, fs);
end

sim_wave = zeros(1,num_samples);

for i = 1:num_waves
    sim_wave = sim_wave + waves(i,:);
end


std(sim_wave);
fprintf('Simulated wave std deviation = %f\n',std(sim_wave));
fprintf('Simulated wave sig wave height = %f\n',4*std(sim_wave));
h = sort(amps');
h_sig = h(round(num_waves*0.67):num_waves,1);
mean(h_sig)

plot(sim_wave)


