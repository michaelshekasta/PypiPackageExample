from src.example import abs_sin


def test_abs_sin():
    assert abs_sin(0) == 0.0
    assert abs_sin(1) == abs_sin(-1)
