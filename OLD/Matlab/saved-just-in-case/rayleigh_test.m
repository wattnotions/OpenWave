y = randraw('rayl', 1, 1e6 );
num_waves = 10;

[amplitudes, edges] = histcounts(y, num_waves);

freq_min = 0.05;
freq_max = 0.67;
freq_range = freq_max-freq_min;

freq_bin_width = freq_range/num_waves;
wave_frequencies      = (freq_min:freq_bin_width:freq_max)';

%print amplitudes, frequencies
[(amplitudes/2000)',wave_frequencies(1:num_waves)]

plot(wave_frequencies(1:num_waves), amplitudes/2000);
xlabel('Wave Frequency (Hz)')
ylabel('Wave Amplitude (M)')


%{
numIntervals = 50;
intervalWidth = (max(y) - min(y))/numIntervals;
x = 0:intervalWidth:15;
ncount = histc(y,x);
relativefreq = ncount/length(y);
bar(x-intervalWidth/2, relativefreq,1)
xlim([min(x) max(x)])
set(gca, 'xtick', x)
xtickangle(45)
%}