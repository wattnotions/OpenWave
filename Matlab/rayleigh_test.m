y = randraw('rayl', 3, 1e5 );
numIntervals = 50;
intervalWidth = (max(y) - min(y))/numIntervals;
x = 0:intervalWidth:15;
ncount = histc(y,x);
relativefreq = ncount/length(y);
bar(x-intervalWidth/2, relativefreq,1)
xlim([min(x) max(x)])
set(gca, 'xtick', x)