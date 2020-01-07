%{
The rotating arm data is timestamped with the runtime of the cpu in
milliseconds.
This script formats these timestamps to seconds and starting from zero
%}


function t = formatTimestamp(timestamps);
    
    t = zeros(length(timestamps),1);
    initial_val = timestamps(1);
    for i=1:length(timestamps)
        t(i) = timestamps(i) - initial_val;
        
    end
    
    t = t/1000;

end