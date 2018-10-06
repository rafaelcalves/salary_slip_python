import pytest
from sample.SalarySlipGenerator import SalarySlipGenerator

@pytest.fixture()
def setup():
    assert True

def test_shouldCallGenerateFor(setup):
    SalarySlipGenerator.generateFor(1)