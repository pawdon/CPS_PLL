import pll
from utils import *
import pytest


def check_correctness(class_name, N):
    freq = 0.4775
    alpha = 0.0100
    beta = 2.5000e-05
    n = N

    selected_class = class_name(freq=freq, alpha=alpha, beta=beta, N=n)
    full = get_data(filename="pilot.csv")
    refer = get_data(filename="nosna.csv")
    blocks = split_data(full, n)
    whole_carr2 = np.array([])
    whole_carr3 = np.array([])

    print("START", "name of class: ", class_name, "blocks: ", N)
    for b in blocks:
        carr2, carr3 = selected_class.process(b)
        whole_carr2 = np.append(whole_carr2, np.array(carr2))
        whole_carr3 = np.append(whole_carr3, np.array(carr3))

    np.testing.assert_almost_equal(refer, whole_carr2[0:len(refer)], decimal=3)


@pytest.mark.parametrize("pll_class", [pll.PllNumPy0, pll.PllNumPy1, pll.PllNumPy2, pll.PllNumPy3, pll.PllNumPy4,
                                       pll.PllNumPy5, pll.PllC1, pll.PllC2, pll.PllC3, pll.PllC2, pll.PllNaive])
@pytest.mark.parametrize("N", [100, 150, 200, 180])
def test_check_correctness(pll_class, N):
    check_correctness(pll_class, N)


if __name__ == "__main__":
    pytest.main()
