function [ freq, latest_theta, carr1, carr2, carr3 ] = PllM1( freq, latest_theta, carr1, carr2, carr3, alpha, beta, N, pilot )

for n = 1:N
    carr1(n) = cos(latest_theta);
    carr2(n) = cos(2 * latest_theta);
    carr3(n) = cos(3 * latest_theta);
    perr = -pilot(n) * sin(latest_theta);
    latest_theta = latest_theta + freq + alpha * perr;
    freq = freq + beta * perr;
end

end

