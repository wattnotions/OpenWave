%{
1.Finds local maxima and minima of time domain signal S
2. Uses these extrema to break signal into individual 'waves' where a wave
is the difference between one minima and the next maxima
3. All wave heights are calculated and the highest third of values are then
averaged to get significant wave height

Arguments:
S : Time domain signal

%}

function [sig_wave_height,avg] = sigWaveCalc(S);



    maxIndices = islocalmax(S);
    minIndices = islocalmin(S);

    t1 = find(maxIndices);
    t2 = find(minIndices);

    %index arrays may not be exact same length
    %find out which has less and use that as end index
    if length(t1) < length(t2)
        max_length = length(t1);
    elseif length(t1) > length(t2)
        max_length = length(t2);
    else
        max_length = length(t2); %they are same length so just pick one
    end

    wave_heights = S(t1(1:max_length))-S(t2(1:max_length));
    wave_heights = sort(wave_heights');
    avg =  mean(wave_heights);
    
    top_third_index = round( length(wave_heights)*0.67);
    sig_wave_height = mean(wave_heights(top_third_index:length(wave_heights)));
   


    % Visualize results
    %{
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
    %}


end