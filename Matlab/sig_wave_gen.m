num_waves = 100; %Number of sine waves to create and add together

%Generate wave amplitudes based on normal distribution
r = normrnd(0,10,[1,num_waves]); %Generate random numbers
amps = r + abs(min(r));        %shift values to positive numbers
%histogram(amps, 100);
std(amps)


%Generate random frequencies between 0.05-0.67Hz
min_freq=0.05;
max_freq=0.67;
n=num_waves;
freqs=min_freq+rand(1,n)*(max_freq-min_freq);

%Generate random phase shifts
min_phase=0;
max_phase=180;
n=num_waves;
phases=min_phase+rand(1,n)*(max_phase-min_phase);



fs = 160;         %sampling frequency in hz
stoptime = 100; %sample length in seconds

waves = zeros(100, (fs*stoptime)+1);  %define matrix to store sine wave vectors in

for i = 1:100 
   waves(i,:) = sineGen(amps(i), freqs(i), phases(i), 100, fs);
end





