function sim_wave = oceanWaveSim(num_waves, amp_scale, fs, stoptime)

    y = randraw('rayl', 1, 1e6 );
   
    [amps, edges] = histcounts(y, num_waves);
    

    freq_min = 0.05;
    freq_max = 0.67;
    freq_range = freq_max-freq_min;

    freq_bin_width = freq_range/num_waves;
    freqs          = (freq_min:freq_bin_width:freq_max)';
    
    amps = amps/max(amps);
    amps = amps*amp_scale;

    %Generate random phase shifts
    min_phase=0;
    max_phase=360;
    n=num_waves;
    phases=min_phase+rand(1,n)*(max_phase-min_phase);



  
    num_samples =  (fs*stoptime)+1;

    waves = zeros(num_waves, num_samples);  %define matrix to store sine wave vectors in

    %generate sine waves and append to waves matrix
    for i = 1:num_waves 
       %fprintf('Amplitude :%0.2f   , Freq : %0.2f, Period : %0.2f, Phase: %0.2f\n',amps(i), freqs(i), 1/freqs(i), phases(i));
       waves(i,:) = sineGen(amps(i), freqs(i), phases(i), stoptime, fs);
    end

    %add all of the generated waves together
    sim_wave = zeros(1,num_samples);
    for i = 1:num_waves
        sim_wave = sim_wave + waves(i,:);
    end


end


