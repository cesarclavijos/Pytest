import sys
import pytest

#@pytest.mark.skipif(condition, *, reason=None)

@pytest.mark.skipif(sys.platform.startswith("darwin"),
    reason="fork not available on Windows",)
def test_spawn_server_using():
    assert True

@pytest.mark.skipif(sys.platform.startswith("win"),
    reason="fork not available on Windows",)
def test__server_using():
    assert True

@pytest.mark.skip(reason='misunderstood the API')
def test_skip():
    assert True

def test_tracers_as_arrays():
    numpy = pytest.importorskip("numpy")

def test_tracers_as_arrays_2():
    numpy = pytest.importorskip("numpy3")