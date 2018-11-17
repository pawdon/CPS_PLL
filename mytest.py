import numpy as np
import math
import time
import pll
import timer


def get_data(filename='pilot.csv'):
    return np.genfromtxt(filename, delimiter=',')


def split_data(data, N):
    split_nr = int(len(data) / N)
    return np.split(data, split_nr)


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


def run():
    N = 100
    freq = 0.4775
    alpha = 0.0100
    beta = 2.5000e-05
    time_measurer = timer.FunTimeMeasurer()

    full = get_data(filename="pilot.csv")
    blocks = split_data(full, N)
    whole_carr2 = np.array([])
    whole_carr3 = np.array([])
    last_theta = 0.0
    theta, carr2, carr3 = pll.get_zeros_lists(N)
    whole_time = 0
    print("START")
    for b in blocks:
        freq, last_theta, carr2, carr3 = time_measurer.run(pll.pll_naive,
                                                           b.tolist(), N, alpha, beta, freq, last_theta, theta, carr2, carr3)
        whole_carr2 = np.append(whole_carr2, np.array(carr2))
        whole_carr3 = np.append(whole_carr3, np.array(carr3))
    print("Total time", time_measurer.get_total_time())
    print("Average time", time_measurer.get_average_time())
    ref = get_data(filename="nosna.csv")
    diff = ref - whole_carr2
    print("sum", np.sum(diff))
    print("diff", diff)


def run_test():
    freq = 0.4775
    alpha = 0.0100
    beta = 2.5000e-05

    pilot = get_data(filename="pilot.csv")
    N = 100000 # len(pilot)
    theta = np.zeros(shape=(N + 1), dtype=np.float)

    for n in range(N):
        perr = -pilot[n] * math.sin(theta[n])
        theta[n + 1] = theta[n] + freq + alpha * perr
        theta[n + 1] = round(theta[n + 1], 4)
        freq = freq + beta * perr

    whole_theta = theta[0:-1]

    ref_theta = get_data(filename="theta.csv")[0:N]
    diff = ref_theta - whole_theta
    print("sum", np.sum(diff))
    print("sum^2", np.sum(diff * diff))
    #print("diff", diff)
    for d in zip(pilot[0:N], ref_theta, theta, diff):
        print("\t", d)


if __name__ == "__main__":
    run()
