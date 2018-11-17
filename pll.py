import math


def pll_naive(pilot, N, alpha, beta, freq, last_theta, theta, carr2, carr3):
    theta[0] = last_theta
    for n in range(N):
        t = theta[n]
        perr = -pilot[n] * math.sin(t)
        t_next = theta[n] + freq + alpha * perr
        freq = freq + beta * perr
        theta[n + 1] = t_next
        carr2[n] = math.cos(2 * t)
        carr3[n] = math.cos(3 * t)
    return freq, theta[-1], carr2, carr3
