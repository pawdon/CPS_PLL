import pll
from utils import *
import pytest


class Correctness:

    def __init__(self, freq, alpha, beta):
        self.freq = freq
        self.latest_theta = 0
        self.alpha = alpha
        self.beta = beta

    def check_correctness(self, class_name, N):
        freq = self.freq
        alpha = self.alpha
        beta = self.beta
        n = N

        plll = class_name(freq=freq, alpha=alpha, beta=beta, N=n)
        full = get_data(filename="pilot.csv")
        refer = get_data(filename="nosna.csv")
        blocks = split_data(full, n)
        whole_carr2 = np.array([])
        whole_carr3 = np.array([])

        print("START", "name of class: ", class_name, "blocks: ", N)
        for b in blocks:
            carr2, carr3 = plll.process(b)
            whole_carr2 = np.append(whole_carr2, np.array(carr2))
            whole_carr3 = np.append(whole_carr3, np.array(carr3))

        np.testing.assert_almost_equal(refer, whole_carr2[0:len(refer)], decimal=3)


if __name__ == "__main__":
    pytest.main()
