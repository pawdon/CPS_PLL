import numpy as np


def get_data(filename):
    return np.genfromtxt(filename, delimiter=',')


def save_data(outputfile, data):
    np.savetxt(outputfile, data, delimiter=',')


def split_data(data, n):
    data_len = len(data)
    split_nr = int(data_len / n)
    underestimated = split_nr * n
    if underestimated != data_len:
        data = np.append(data, np.zeros(shape=underestimated + n - data_len))
        split_nr += 1
    return np.split(data, split_nr)