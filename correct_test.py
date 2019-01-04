import pll
from utils import *
import pytest


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

    np.testing.assert_almost_equal(full[256:], whole_carr1[256:len(full)], decimal=1)


@pytest.mark.parametrize("pll_class", [pll.PllNaive, pll.PllNumPy0, pll.PllNumPy1, pll.PllNumPy2, pll.PllNumPy3,
                                       pll.PllNumPy4, pll.PllNumPy5, pll.PllC1, pll.PllC2, pll.PllC3])
@pytest.mark.parametrize("N", [256, 256000])
def test_check_correctness(pll_class, N):
    check_correctness(pll_class, N)


if __name__ == "__main__":
    pytest.main()
