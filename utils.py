import numpy as np


def get_data(filename):
    """
    Get a NumPy array from a file
    :param filename: a name of a file to read
    :return: a NumPy array
    """
    return np.genfromtxt(filename, delimiter=',')


def save_data(outputfile, data):
    """
    Save NumPy to a file
    :param outputfile: a name of a file
    :param data: a NumPy array to write
    :return:
    """
    np.savetxt(outputfile, data, delimiter=',')


def split_data(data, n):
    """
    Split data to blocks of length n. If mod(len(data), n) != 0, expand it by arrays of 0
    :param data: data to split
    :param n: length of a single block
    :return: an array of arrays of length n
    """
    data_len = len(data)
    split_nr = int(data_len / n)
    underestimated = split_nr * n
    if underestimated != data_len:
        data = np.append(data, np.zeros(shape=underestimated + n - data_len))
        split_nr += 1
    return np.split(data, split_nr)
