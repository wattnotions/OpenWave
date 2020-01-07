
fs = 20;
file_names = ["20cm_3v","20cm_4.5v", "30cm_3v", "30cm_4.5v", "40cm_3v", "40cm_4.5v"]


for i=1:6
    
    % read accel data from csv file
    T = readtable('../test_data/rotating_arm_data/'+file_names(i)+'.csv');
    z_accel = table2array(T(:,3)); %z_accel
    timestamps = table2array(T(:,9)); %timestamps

    t = formatTimestamp(timestamps); %X axis (milliseconds)

    %convert t array to duration vector
    dur_t = seconds(t);

    %get signal length
    signal_length = t(end)-t(1);

    %the original timestamp data is not accurately spaced, create a vector with
    %correct timing (will fit to accel data with interpolation)
    correct_t = seconds(0:0.05:floor(signal_length));

    %filter out high frequency noise
    %z_accel = lowpass(z_accel,0.2, fs,'Steepness',0.96);
   
    %convert accel to displacement
    disp = accel2Disp(z_accel,t);    

    %create a timetable with the accel data and timestamps
    TT = array2timetable(disp, 'RowTimes', seconds(t));

    %create new table using interpolation to correct timestamp timing offsets
    TT2 = retime(TT,correct_t,'linear');
    TT2(1:5,:);

    %remove low freq noise caused by double integration
    [filtered_disp, fil] = highpass(TT2,0.1,'Steepness',0.85);

    %plotFFT(fs, length(filtered_disp.Variables), filtered_disp.Variables)
    
    [sig_wave_height, avg_wave_height] = (sigWaveCalc(filtered_disp.Variables));
    
    avg_wave_height = 100*avg_wave_height; %convert from metres to cm
    
    %get calculated height from file name
    current_file = char(file_names(i));
    calc_height =  current_file(1:2);
    calc_height = str2num(calc_height);
    calc_height = calc_height*2; 
    
    percent_error = 100*((calc_height - avg_wave_height) / avg_wave_height);

    

    fprintf('Calculated = %0.2f   Measured = %0.2f   diff = %0.2f\n',calc_height,avg_wave_height,percent_error);
    

    %plot displacement signal
    %{
    figure(1003)
    plot(filtered_disp.Time,filtered_disp.Variables);
    title('Output displacement')
    xlabel('Time (Seconds)')
    %}
    
end