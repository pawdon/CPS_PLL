import check_corr
import pll

import pytest


@pytest.mark.parametrize("pll_class", [pll.PllNumPy0, pll.PllNumPy1, pll.PllNumPy2, pll.PllNumPy3, pll.PllNumPy4,
                                       pll.PllNumPy5, pll.PllC1, pll.PllC2, pll.PllC3, pll.PllC2, pll.PllNaive])
@pytest.mark.parametrize("N", [100, 150, 200, 180])

def test_param(pll_class, N):
    cor_object = check_corr.Correctness(0.4775, 0.0100, 2.5000e-05)
    cor_object.check_correctness(pll_class, N)


if __name__ == "__main__":
    pytest.main()


