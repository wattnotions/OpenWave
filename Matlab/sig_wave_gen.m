%Generate wave amplitudes based on normal distribution
r = normrnd(0,10,[1,100]); %Generate random numbers
amps = r + abs(min(r));        %shift values to positive numbers
%histogram(amps, 100);
std(amps)


%Generate random frequencies
min_freq=0.05;
max_freq=0.67;
n=100;
freqs=min_freq+rand(1,n)*(max_freq-min_freq)

%Generate random phase shifts
min_phase=0;
max_phase=180;
n=100;
phases=min_phase+rand(1,n)*(max_phase-min_phase)



for i = 1:100 
   waves = sineGen(amps(i), freqs(i), phases(i), 100)];
end



