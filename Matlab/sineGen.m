function y = sineGen(amplitude, freq, phase, stoptime, fs)

    
    dt = 1/fs; % seconds per sample 
    t = (0:dt:stoptime)'; % seconds 
    F = freq; % Sine wave frequency (hertz)
    p_shift = deg2rad(phase);
    y = amplitude*sin(2*pi*F*t + p_shift);
  

end