%%% read accel data from csv file
T = readtable('../test_data/rotating_arm_data/20cm_3v.csv');
z_accel = table2array(T(:,3)); %z_accel
timestamps = table2array(T(:,9)); %timestamps


formatted_t = formatTimestamp(timestamps);


