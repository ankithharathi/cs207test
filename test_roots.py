import pytest
import roots

def test_quadroots_result():
    assert roots.quad_roots(1.0, 1.0, -12.0) == ((3+0j), (-4+0j))

def test_quadroots_types():
    with pytest.raises(TypeError):
        roots.quad_roots("", "green", "hi")

def test_quadroots_zerocoeff():
    with pytest.raises(ValueError):
        roots.quad_roots(a=0.0)


def test_linearroots_result():
    assert roots.linear_roots(1.0, 2.0) == -2.0

def test_linearroots_types():
    with pytest.raises(TypeError):
        roots.linear_roots("", "green", "hi")

def test_linearoots_zerocoeff():
    with pytest.raises(ValueError):
        roots.linear_roots(a=0.0)