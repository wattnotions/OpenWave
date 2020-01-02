function displacement = accel2Disp(accel, fs,t)

    
    dt=1/fs;
    stoptime = (length(accel)-1)/fs;
   % t = (0:dt:stoptime)'; % seconds 
    
    accel = accel-mean(accel);
    
    
    velocity = cumtrapz(t,accel);
    velocity = velocity-mean(velocity);
   
    
    
    displacement = cumtrapz(t,velocity);
   
    
    hold off
    figure(2005)
    
    
    h = tiledlayout(3,1);
    
    nexttile
    plot(t, accel,'b')
    title('Acceleration')
    hold on
    
    nexttile
    plot(t, velocity,'r')
    title('Velocity')
    
    nexttile
    plot(t,displacement,'g')
    title('Displacement')
    
    %legend('Displacement','velocity', 'acceleration')
    xlabel('Time (Seconds)');
    
    title(h, 'Acceleration to Displacement')

end