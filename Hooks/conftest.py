import pytest
import time

@pytest.hookimpl(hookwrapper=True)
def pytest_collection(session):
    collect_timeout = 5
    collect_begin_time = time.time()
    yield
    collect_end_time = time.time()
    c_time = collect_end_time - collect_begin_time
    if c_time > collect_timeout:
        raise Exception('Collection timeout.')

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    # called for running each test in 'a' directory
    time.sleep(1)
    print("setting up", item)

#@pytest.hookimpl(trylast=True)
#def pytest_runtest_setup(items):
    # called for running each test in 'a' directory
    #a = type(items)
    #print("The total of teswt cases were", a)

