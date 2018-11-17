import numpy as np
import math


def get_zeros_lists(N):
    theta = [0.0 for _ in range(N)]
    carr2 = [1.0 for _ in range(N)]
    carr3 = [1.0 for _ in range(N)]
    return theta, carr2, carr3


def pll_naive(pilot, N, alpha, beta, freq, latest_theta, theta, carr2, carr3):
    for n in range(N):
        carr2[n] = math.cos(2 * latest_theta)
        carr3[n] = math.cos(3 * latest_theta)
        perr = -pilot[n] * math.sin(latest_theta)
        latest_theta += freq + alpha * perr
        freq += beta * perr
    return freq, latest_theta, carr2, carr3


def pll_numpy(pilot, N, alpha, beta, freq, last_theta, theta, carr2, carr3):
    theta[0] = last_theta
    t = last_theta
    for n in range(N):
        perr = -pilot.item(n) * np.sin(t)
        t += freq + alpha * perr
        freq = freq + beta * perr
        theta.itemset(n + 1, t)
    carr2 = np.cos(2 * theta[0:-1])
    carr3 = np.cos(3 * theta[0:-1])
    return freq, theta.item(-1), carr2, carr3
