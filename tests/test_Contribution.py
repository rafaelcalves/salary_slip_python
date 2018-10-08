import pytest

from sample.Contribution import Contribution

@pytest.fixture(autouse=True)
def contribution():
    return Contribution(11000, .2, .4)

def test_isTaxedShouldReturnTrueWhenAnnualGrossSalaryBiggerThanUntaxedRoof(contribution):
    assert contribution.isTaxed(12000)

def test_isTaxedShouldReturnFalseWhenAnnualGrossSalaryLowerThanUntaxedRoof(contribution):
    assert not contribution.isTaxed(10000)

def test_getTaxedAmountShouldReturn1000WhenAnnualGrossSalary12000(contribution):
    assert contribution.getTaxedAmountFor(12000) == 1000

def test_applyLowerRateToShouldReturn20WhenTaxedAmount1200(contribution):
    assert contribution.applyLowerRateTo(1200) == 20

def test_applyHigherRateToShouldReturn40WhenTaxedAmount1200(contribution):
    assert contribution.applyHigherRateTo(1200) == 40
