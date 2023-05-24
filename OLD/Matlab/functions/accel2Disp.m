%{
1. Takes acceleration time domain signal and integrates it twice
2. This gives you a displacement signal

Arguments:
accel : time domain acceleration signal
t    :  sample timestamps in seconds(first sample start at time=0)

%}

function [displacement, velocity] = accel2Disp(accel,t);
    

   
   
    accel = accel-mean(accel);
    velocity = cumtrapz(t,accel);
    velocity = velocity-mean(velocity);

    displacement = cumtrapz(t,velocity);
    displacement = displacement-mean(displacement);
    
    
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