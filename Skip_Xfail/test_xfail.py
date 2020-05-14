import pytest
import sys
import numpy
#@pytest.mark.xfail(condition=None, *, reason=None, raises=None, run=True, strict=False)

@pytest.mark.xfail(
    reason="flaky test #123", strict=True
)
def test_no_condition():
    assert True

@pytest.mark.xfail(
    reason="flaky test #123", strict=True
)
def test_no_condition2():
    assert False



@pytest.mark.xfail(sys.platform.startswith("win"), 
    reason="not found", strict=False)
def test_sys_1():
    assert True


@pytest.mark.xfail(sys.platform.startswith("darwin"), 
    reason="not found", strict=False)
def test_sys_2():
    assert True


@pytest.mark.xfail(sys.platform.startswith("darwin"), 
    reason="It's the version for future implementations",)
def test_sys_3():
    assert True


def test_particle_splitting():
    if numpy.__version__ < "0":
        pytest.xfail("split computation fails with numpy < 1.13")