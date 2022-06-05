from OSE_assignment1.quadratures import midpoint, trapezoidal


def test_midpoint():
    assert midpoint(0, 1, lambda x: x**2) == 0.25


def test_trapezoidal():
    assert trapezoidal(0,1,lambda x: x**2) == 0
