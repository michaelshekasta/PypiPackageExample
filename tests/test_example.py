import numpy as np

from pypi_package_example.example import abs_sin, abs_pearson


def test_abs_sin():
    assert abs_sin(0) == 0.0
    assert abs_sin(1) == abs_sin(-1)


def test_abs_pearson():
    assert abs_pearson(np.asarray([1, 2]), np.asarray([-1, -2])) == (1.0, 1.0)
