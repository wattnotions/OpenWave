function disp_time_data = acc2disp(acc_time_data,dt)
% acc_time_data should be acceleration amplitudes evenly spaced in time
% dt in units of seconds per sample
N1 = length(acc_time_data);
  N = 2^nextpow2(N1);
  if N > N1
      acc_time_data(N1+1:N) = 0; % pad array with 0's
  end
  df = 1 / (N*dt); % frequency increment
  Nyq = 1 / (2*dt); % Nyquist frequency
  acc_freq_data = fftshift(fft(acc_time_data));
  disp_freq_data = zeros(size(acc_freq_data));
  f = -Nyq:df:Nyq-df; % I think this is how fftshift organizes it
  for i = 1 : N
      if f(i) ~= 0
          disp_freq_data(i) = acc_freq_data(i)/(2*pi*f(i)*sqrt(-1))^2;
      else
          disp_freq_data(i) = 0;
      end
  end
  disp_time_data = ifft(ifftshift(disp_freq_data));    
  disp_time_data = disp_time_data(1:N1);
  
return