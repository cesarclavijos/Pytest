from pytest_bdd import scenarios, parsers, given, when, then, scenario

from cucumbers import CucumberBasket


#scenarios('../features/cucumbers.feature')


EXTRA_TYPES = {
    'Number': int,
}

@scenario('../features/cucumbers.feature', 'Add cucumbers to a basket')
def test_add():
    pass

@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers', extra_types={'Number': int,}))
def basket(initial):
    return CucumberBasket(initial_count=initial)


@when(parsers.cfparse('"{some:Number}" cucumbers are added to the basket', extra_types=EXTRA_TYPES))
def add_cucumbers(basket, some):
    basket.add(some)


@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers', extra_types=EXTRA_TYPES))
def basket_has_total(basket, total):
    assert basket.count == total


@scenario('../features/cucumbers.feature', 'Remove cucumbers from a basket')
def test_remove():
    pass

@given(parsers.cfparse('the basket has "{initial:Number}" cucumbers', extra_types=EXTRA_TYPES))
def basket(initial):
    return CucumberBasket(initial_count=initial)

@when(parsers.cfparse('"{some:Number}" cucumbers are removed from the basket', extra_types=EXTRA_TYPES))
def remove_cucumbers(basket, some):
    basket.remove(some)


@then(parsers.cfparse('the basket contains "{total:Number}" cucumbers', extra_types=EXTRA_TYPES))
def basket_has_total(basket, total):
    assert basket.count == total