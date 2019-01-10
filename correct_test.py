import pll
from utils import *
import pytest
import os
import math
import json
from trigonometric_lut import LUT_ARRAY_LENGTH


def check_correctness(class_name, N):
    freq = 2*np.pi*19/256
    alpha = 0.0100
    beta = 2.5000e-05
    n = N

    selected_class = class_name(freq=freq, alpha=alpha, beta=beta, N=n)
    full = get_data(filename="real_pilot_256000.csv")
    blocks = split_data(full, n)
    whole_carr1 = np.array([])
    whole_carr2 = np.array([])
    whole_carr3 = np.array([])

    print("START", "name of class: ", class_name, "blocks: ", N)
    for b in blocks:
        carr1, carr2, carr3 = selected_class.process(b)
        whole_carr1 = np.append(whole_carr1, np.array(carr1))
        whole_carr2 = np.append(whole_carr2, np.array(carr2))
        whole_carr3 = np.append(whole_carr3, np.array(carr3))

    # print("*********************************************************")
    # print(np.max(np.abs(whole_carr1[256:len(full)] - full[256:])))
    # print("*********************************************************")
    correct_file = 'results/correct.json'
    if not os.path.exists(correct_file):
        with open(correct_file, 'w'):
            pass
    matlab_carr1 = get_data(filename="matlab/carr1.csv")
    matlab_carr2 = get_data(filename="matlab/carr2.csv")
    matlab_carr3 = get_data(filename="matlab/carr3.csv")

    diff1 = whole_carr1[256:len(whole_carr1)] - matlab_carr1[256:]
    diff2 = whole_carr2[256:len(whole_carr2)] - matlab_carr2[256:]
    diff3 = whole_carr3[256:len(whole_carr3)] - matlab_carr3[256:]

    max_diff1 = np.max(np.abs(diff1))
    max_diff2 = np.max(np.abs(diff2))
    max_diff3 = np.max(np.abs(diff3))

    rmse1 = math.sqrt(np.sum(diff1 * diff1) / len(diff1))
    rmse2 = math.sqrt(np.sum(diff2 * diff2) / len(diff2))
    rmse3 = math.sqrt(np.sum(diff3 * diff3) / len(diff3))

    data = {"Algorithm info": class_name.info(),
            "Block length": n,
            "Max diff carr 1": max_diff1,
            "Max diff carr 2": max_diff2,
            "Max diff carr 3": max_diff3,
            "RMSE carr 1": rmse1,
            "RMSE carr 2": rmse2,
            "RMSE carr 3": rmse3}
    print(data)
    with open(correct_file, 'a') as f:
        text = json.dumps(data)
        f.write(text + "\n")

    np.testing.assert_almost_equal(full[256:], whole_carr1[256:len(full)], decimal=1)


@pytest.mark.parametrize("pll_class", [pll.PllNumPy5, pll.PllC3, pll.PllC4])
@pytest.mark.parametrize("N", [256, 256000])
def test_check_correctness(pll_class, N):
    check_correctness(pll_class, N)


if __name__ == "__main__":
    pytest.main()
