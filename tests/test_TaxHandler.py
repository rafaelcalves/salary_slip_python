import pytest
from sample.TaxHandler import TaxHandler

def test_getMonthlyShouldReturn8dot33WhenValue100():
    monthlyValue = TaxHandler.getMonthlyValueFor(100)
    assert monthlyValue == 8.33

def test_applyNationalInsuranceToAmountShouldReturn12WhenValue1200():
    nationalInsurance = TaxHandler.applyNationalInsuranceLowerRateToAmount(1200)
    assert nationalInsurance == 12

def test_applyTaxPayableToAmountShouldReturn20WhenValue1200():
    nationalInsurance = TaxHandler.applyTaxPayableLowerRateToAmount(1200)
    assert nationalInsurance == 20
