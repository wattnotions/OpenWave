function y = sineGen(amplitude, freq, phase, stoptime)

    fs = 2048; % Sampling frequency (samples per second) 
    dt = 1/fs; % seconds per sample 
    t = (0:dt:stoptime)'; % seconds 
    F = freq; % Sine wave frequency (hertz)
    p_shift = deg2rad(phase);
    y = sin(amplitude*pi*F*t + p_shift);

end