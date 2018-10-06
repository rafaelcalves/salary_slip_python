import pytest

from sample.SalarySlipGenerator import SalarySlipGenerator
from sample.Employee import Employee
from sample.SalarySlip import SalarySlip


@pytest.fixture(autouse=True)
def setup():
    employee = Employee(1, "John J Doe", 5000)
    return employee

def test_shouldReturnASalarySlipInstance():
    assert isinstance(SalarySlipGenerator.generateFor(setup), SalarySlip)

def test_monthlySalarySlipShouldBe416dot67():
    salarySlip = SalarySlipGenerator.generateFor(setup)
    assert salarySlip.monthlyGrossSalary == 416.67
