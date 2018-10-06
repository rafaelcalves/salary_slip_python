import pytest

from sample.Employee import Employee
from sample.SalarySlipGenerator import SalarySlipGenerator


@pytest.fixture()
def setupEmployee5000(request):
    return Employee(12345, "John J Doe", 5000)

@pytest.fixture()
def setupEmployee9060(request):
    return Employee(12345, "John J Doe", 9060)

@pytest.fixture()
def setupEmployee12000(request):
    return Employee(12345, "John J Doe", 12000)

def test_monthlySalarySlipShouldBe416dot67WhenAnnualSalary5000(setupEmployee5000):
    salarySlip = SalarySlipGenerator.generateFor(setupEmployee5000)
    assert salarySlip.monthlyGrossSalary == 416.67

def test_nationalInsuranceShouldBeZeroWhenAnnualSalary5000(setupEmployee5000):
    salarySlip = SalarySlipGenerator.generateFor(setupEmployee5000)
    assert salarySlip.nationalInsurance == 0

def test_nationalInsuranceShouldBe10WhenAnnualSalary9060(setupEmployee9060):
    salarySlip = SalarySlipGenerator.generateFor(setupEmployee9060)
    assert salarySlip.nationalInsurance == 10.0

def test_taxPayableShouldBeZeroWhenAnnualSalary9060(setupEmployee9060):
    salarySlip = SalarySlipGenerator.generateFor(setupEmployee9060)
    assert salarySlip.taxPayable == 0

def test_taxFreeAllowanceShouldBeZeroWhenAnnualSalary9060(setupEmployee9060):
    salarySlip = SalarySlipGenerator.generateFor(setupEmployee9060)
    assert salarySlip.taxFreeAllowance == 0

def test_taxableIncomeShouldBeZeroWhenAnnualSalat9060(setupEmployee9060):
    salarySlip = SalarySlipGenerator.generateFor(setupEmployee9060)
    assert salarySlip.taxableIncome == 0

def test_taxPayableShouldBe16do67WhenAnnualSalary12000(setupEmployee12000):
    salarySlip = SalarySlipGenerator.generateFor(setupEmployee12000)
    assert salarySlip.taxPayable == 16.67

def test_taxFreeAllowanceShouldBe916dot67WhenAnnualSalary12000(setupEmployee12000):
    salarySlip = SalarySlipGenerator.generateFor(setupEmployee12000)
    assert salarySlip.taxFreeAllowance == 916.67

def test_taxableIncomeShouldBe83dot33WhenAnnualSalat12000(setupEmployee12000):
    salarySlip = SalarySlipGenerator.generateFor(setupEmployee12000)
    assert  salarySlip.taxableIncome == 83.33