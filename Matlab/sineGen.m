function y = sineGen(amplitude, freq, phase)

    fs = 2048; % Sampling frequency (samples per second) 
    dt = 1/fs; % seconds per sample 
    StopTime = 0.25; % seconds 
    t = (0:dt:StopTime)'; % seconds 
    F = freq; % Sine wave frequency (hertz)
    p_shift = deg2rad(phase);
    y = sin(amplitude*pi*F*t + p_shift);

end