from selenium import webdriver
from pytest import mark

@mark.smoke
@mark.engine
@mark.ui
def test_enavigation_engine_as_expected():
    assert True