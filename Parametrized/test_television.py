from pytest import mark
from selenium import webdriver

@mark.parametrize('tv_brand', [
        ('Samsung'),
        ('Sony'),
        ('Vizio')
    ]
)
def test_television_turns_on2(tv_brand):
    print(f"{tv_brand} turns on as expected")


#def test_browser_can_navigate_to_training_ground(browser):
#    browser.get("http://www.python.org")
#    assert "Python" in browser.title

def test_television_turns_on_from_fixture(tv_brand_from_fixture):
    print(f"{tv_brand_from_fixture} turns on as expected")