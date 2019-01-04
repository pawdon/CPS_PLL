%function [  ] = PLL_MATLAB_TEST(  )
filename = 'efficiency.m.json';
fid = fopen(filename, 'w');
fclose(fid);

block_lengths = [256, 2560, 25600, 256000];
init_freq = 2*pi*19/256;
init_theta = 0;
alpha = 0.0100;
beta = 2.5000e-05;

pilot = csvread('../real_pilot_256000.csv');
%pilot = csvread('../real_pilot_2599999.csv');

for N=block_lengths
    freq = init_freq;
    latest_theta = init_theta;
    carr1 = ones(N, 1);
    carr2 = ones(N, 1);
    carr3 = ones(N, 1);
    whole_carr1 = [];
    whole_carr2 = [];
    whole_carr3 = [];

    blocks = split_data(pilot, N);
    whole_time = 0;
    loops_nr = 0;
    sprintf('START')
    sprintf('Block length = %d', N)
    for b=blocks
        tic
        [freq, latest_theta, carr1, carr2, carr3] = PllM1( freq, latest_theta, carr1, carr2, carr3, alpha, beta, N, b );
        t = toc;
        whole_time = whole_time + t;
        loops_nr = loops_nr + 1;
        whole_carr1 = [whole_carr1; carr1];
        whole_carr2 = [whole_carr2; carr2];
        whole_carr3 = [whole_carr3; carr3];
    end
    sprintf('STOP')

    real_time_percent = whole_time * 100 * 256000 / length(pilot);
    sprintf('Total time %f', whole_time)
    sprintf('Real time percent %f', real_time_percent)
    
    diff = pilot(257:end) - whole_carr1(257:length(pilot));

    sprintf('Max diff %f', max(diff))

    fid = fopen(filename, 'a');
    fprintf(fid, '{"Algorithm info": "PLL Matlab", "Block length": %d, "Total time": %f, "Real time percent": %f}\n', N, whole_time, real_time_percent);
    fclose(fid);
end

%end

