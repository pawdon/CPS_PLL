import numpy as np
import math
from trigonometric_lut import *


def get_default_lists(N):
    theta = [0.0 for _ in range(N)]
    carr2 = [1.0 for _ in range(N)]
    carr3 = [1.0 for _ in range(N)]
    return theta, carr2, carr3


def get_default_np_arrays(N):
    theta = np.zeros(shape=N, dtype=np.float)
    carr2 = np.ones(shape=N, dtype=np.float)
    carr3 = np.ones(shape=N, dtype=np.float)
    return theta, carr2, carr3


def pll_naive(pilot, N, alpha, beta, freq, latest_theta, carr2, carr3, theta):
    for n in range(N):
        carr2[n] = math.cos(2 * latest_theta)
        carr3[n] = math.cos(3 * latest_theta)
        perr = -pilot[n] * math.sin(latest_theta)
        latest_theta += freq + alpha * perr
        freq += beta * perr
    return freq, latest_theta, carr2, carr3


def pll_numpy_ver1(pilot, N, alpha, beta, freq, latest_theta, carr2, carr3, theta):
    for n in range(N):
        carr2.itemset(n, math.cos(2 * latest_theta))
        carr3.itemset(n, math.cos(3 * latest_theta))
        perr = -pilot.item(n) * math.sin(latest_theta)
        latest_theta += freq + alpha * perr
        freq += beta * perr
    return freq, latest_theta, carr2, carr3


def pll_numpy_ver2(pilot, N, alpha, beta, freq, latest_theta, carr2, carr3, theta):
    for n in range(N):
        carr2.itemset(n, np.cos(2 * latest_theta))
        carr3.itemset(n, np.cos(3 * latest_theta))
        perr = -pilot.item(n) * np.sin(latest_theta)
        latest_theta += freq + alpha * perr
        freq += beta * perr
    return freq, latest_theta, carr2, carr3


def pll_numpy_ver3(pilot, N, alpha, beta, freq, latest_theta, carr2, carr3, theta):
    for n in range(N):
        theta.itemset(n, latest_theta)
        perr = -pilot.item(n) * np.sin(latest_theta)
        latest_theta += freq + alpha * perr
        freq += beta * perr
    carr2 = np.cos(2 * theta)
    carr3 = np.cos(3 * theta)
    return freq, latest_theta, carr2, carr3


def pll_numpy_ver4(pilot, N, alpha, beta, freq, latest_theta, carr2, carr3, theta):
    for pil, c2, c3 in zip(np.nditer(pilot, op_flags=['readonly']),
                           np.nditer(carr2, op_flags=['writeonly']),
                           np.nditer(carr3, op_flags=['writeonly'])):
        c2[...] = math.cos(2 * latest_theta)
        c3[...] = math.cos(3 * latest_theta)
        perr = -pil * math.sin(latest_theta)
        latest_theta += freq + alpha * perr
        freq += beta * perr
    return freq, latest_theta, carr2, carr3


def pll_numpy_ver5(pilot, N, alpha, beta, freq, latest_theta, carr2, carr3, theta):
    for n in range(N):
        carr2.itemset(n, Lut.cos(2 * latest_theta))
        carr3.itemset(n, Lut.cos(3 * latest_theta))
        perr = -pilot.item(n) * Lut.sin(latest_theta)
        latest_theta += freq + alpha * perr
        freq += beta * perr
    return freq, latest_theta, carr2, carr3
