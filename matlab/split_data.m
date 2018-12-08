function [ splitted ] = split_data( data, N )

splitted = [];
transposed = transpose(data);

data_len = length(transposed);
split_nr = floor(data_len / N);
underestimated = split_nr * N;
if underestimated < data_len
    transposed = [transposed, zeros(1, underestimated + N - data_len)];
end

start = 1;
stop = N;
data_len = length(transposed);

while start < data_len
    splitted = [splitted; transposed(start:stop)];
    start = start + N;
    stop = stop + N;
end
splitted = transpose(splitted);

end

