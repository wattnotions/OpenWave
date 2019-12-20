function sim_wave = oceanWaveSim(num_waves, amp_std_dev, fs, stoptime)

   

    %Generate wave amplitudes based on normal distribution
    r = normrnd(0,1,[1,num_waves]); %Generate random numbers
    amps = r + abs(min(r));        %shift values to positive numbers
    
    %figure(1)
    %histogram(amps, 100);
    %grid



    %Generate random frequencies between 0.05-0.67Hz
    min_freq=0.05;
    max_freq=0.67;
    n=num_waves;
    freqs=min_freq+rand(1,n)*(max_freq-min_freq);
    %histogram(freqs, 100);

    %Generate random phase shifts
    min_phase=0;
    max_phase=360;
    n=num_waves;
    phases=min_phase+rand(1,n)*(max_phase-min_phase);



  
    num_samples =  (fs*stoptime)+1;

    waves = zeros(num_waves, num_samples);  %define matrix to store sine wave vectors in

    %generate sine waves and append to waves matrix
    for i = 1:num_waves 
       waves(i,:) = sineGen(amps(i), freqs(i), phases(i), stoptime, fs);
    end

    %add all of the generated waves together
    sim_wave = zeros(1,num_samples);
    for i = 1:num_waves
        sim_wave = sim_wave + waves(i,:);
    end


end


