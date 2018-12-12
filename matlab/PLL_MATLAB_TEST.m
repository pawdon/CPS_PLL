function [  ] = PLL_MATLAB_TEST(  )
filename = 'efficiency.m.json';
fid = fopen(filename, 'w');
fclose(fid);

block_lengths = [100, 150];
init_freq = 0.4775;
init_theta = 0;
alpha = 0.0100;
beta = 2.5000e-05;

pilot = csvread('pilot.csv');

for N=block_lengths
    freq = init_freq;
    latest_theta = init_theta;
    carr2 = ones(N, 1);
    carr3 = ones(N, 1);
    whole_carr2 = [];
    whole_carr3 = [];

    blocks = split_data(pilot, N);
    whole_time = 0;
    loops_nr = 0;
    sprintf('START')
    sprintf('Block length = %d', N)
    for b=blocks
        tic
        [freq, latest_theta, carr2, carr3] = PllM1( freq, latest_theta, carr2, carr3, alpha, beta, N, b );
        t = toc;
        whole_time = whole_time + t;
        loops_nr = loops_nr + 1;
        whole_carr2 = [whole_carr2; carr2];
        whole_carr3 = [whole_carr3; carr3];
    end
    sprintf('STOP')

    sprintf('Total time %f', whole_time)
    sprintf('Average time %f', whole_time / loops_nr)

    ref_carr2 = csvread('nosna.csv');
    diff = ref_carr2 - whole_carr2(1:length(ref_carr2));

    sprintf('Max diff %f', max(diff))
    sprintf('Sum diff %f', sum(diff))

    fid = fopen(filename, 'a');
    fprintf(fid, '{"Algorithm info": "PLL Matlab", "Block length": %d, "Total time": %f, "Average time": %f}\n', N, whole_time, whole_time / loops_nr);
    fclose(fid);
end

end

