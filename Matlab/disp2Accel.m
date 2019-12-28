function accel = disp2Accel(displacement, fs)

    
    dt=1/fs;
    stoptime = (length(displacement)-1)/fs;
    t = (0:dt:stoptime)'; % seconds 
    
    
    velocity = gradient(displacement(:)) ./ gradient(t(:));
    accel = gradient(velocity(:)) ./ gradient(t(:));
    
    hold off
    figure(1)
    

    
    h = tiledlayout(3,1);
    nexttile
    plot(t,displacement,'g')
    title('Displacement')
    
    hold on
    nexttile
    plot(t, velocity,'r')
    title('Velocity')
    
    nexttile
    plot(t, accel,'b')
    title('Acceleration')
    %legend('Displacement','velocity', 'acceleration')
    xlabel('Time (Seconds)');
    
    title(h, 'Displacement to Acceleration')

end