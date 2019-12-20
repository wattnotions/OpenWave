num_waves = 10000;
fs = 4;
dt=1/fs;
stoptime = 60;
sample_length = (fs*stoptime)+1;


S = oceanWaveSim(num_waves, 1, fs, stoptime);
plotFFT(fs, sample_length, S);


%Plot surface displacement
figure(3)
t = (0:dt:stoptime)'; % seconds 

%plot(t,S);
%yline((4*std(S))- abs(min(S)));
% Find local maxima and minima
maxIndices = islocalmax(S);
minIndices = islocalmin(S);

% Visualize results
clf
plot(S,'Color',[109 185 226]/255,'DisplayName','Input data')
hold on

% Plot local maxima
plot(find(maxIndices),S(maxIndices),'^','Color',[217 83 25]/255,...
    'MarkerFaceColor',[217 83 25]/255,'DisplayName','Local maxima')

% Plot local minima
plot(find(minIndices),S(minIndices),'v','Color',[237 177 32]/255,...
    'MarkerFaceColor',[237 177 32]/255,'DisplayName','Local minima')
title(['Number of extrema: ' num2str(nnz(maxIndices)+nnz(minIndices))])
hold off
legend
