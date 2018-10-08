import pytest

from sample.tuples.Employee import Employee
from sample.tuples.SalarySlip import SalarySlip


@pytest.fixture()
def salarySlipBaseEmployee():
    return getBaseSalarySlip(getBaseEmployee())


def getBaseEmployee():
    return Employee(12345, "John J Doe", 12000)


def getEmployeeSameGrossSalary():
    return Employee(54321, "Doe J John", 12000)


def getEmployeeFullDifferent():
    return Employee(54321, "Doe J John", 10000)


def getBaseSalarySlip(employee):
    return SalarySlip(employee, 1000, 39.40, 916.67, 83.33, 16.67)


def getDifferentMonthlySalary(employee):
    return SalarySlip(employee, 1500, 39.40, 916.67, 83.33, 16.67)


def getDifferentNationalInsurance(employee):
    return SalarySlip(employee, 1000, 50, 916.67, 83.33, 16.67)


def getDifferentTaxFreeAllowance(employee):
    return SalarySlip(employee, 1000, 39.40, 1000, 83.33, 16.67)


def getDifferentTaxableIncome(employee):
    return SalarySlip(employee, 1000, 39.40, 916.67, 100, 16.67)


def getDifferentTaxPayable(employee):
    return SalarySlip(employee, 1000, 39.40, 916.67, 83.33, 20)


def test_salarySlipForBaseEmployeeShouldBeEqualsToSalarySlipForEmployeeSameGrossSalary(salarySlipBaseEmployee):
    salarySlipSameGrossSalaryEmployee = getBaseSalarySlip(getEmployeeSameGrossSalary())
    assert salarySlipBaseEmployee.__eq__(salarySlipSameGrossSalaryEmployee)


def test_salarySlipForBaseEmployeeShouldBeNotEqualsToSalarySlipForEmployeeFullDifferentEmployee(salarySlipBaseEmployee):
    salarySlipFullDifferentEmployee = getBaseSalarySlip(getEmployeeFullDifferent())
    assert salarySlipBaseEmployee.__ne__(salarySlipFullDifferentEmployee)


def test_salarySlipShouldBeNotEqualsIfMonthlySalaryIsDifferent(salarySlipBaseEmployee):
    salarySlipDifferentMonthlySalary = getDifferentMonthlySalary(getBaseEmployee())
    assert salarySlipBaseEmployee.__ne__(salarySlipDifferentMonthlySalary)


def test_salarySlipShouldBeNotEqualsIfNationalInsuranceIsDifferent(salarySlipBaseEmployee):
    salarySlipDifferentNationalInsurance = getDifferentNationalInsurance(getBaseEmployee())
    assert salarySlipBaseEmployee.__ne__(salarySlipDifferentNationalInsurance)

def test_salarySlipShouldBeNotEqualsIfTaxFreeAllowanceIsDifferent(salarySlipBaseEmployee):
    salarySlipDifferentTaxFreeAllowance = getDifferentTaxFreeAllowance(getBaseEmployee())
    assert salarySlipBaseEmployee.__ne__(salarySlipDifferentTaxFreeAllowance)


def test_salarySlipShouldBeNotEqualsIfTaxableIncomeIsDifferent(salarySlipBaseEmployee):
    salarySlipDifferentTaxableIncome = getDifferentTaxableIncome(getBaseEmployee())
    assert salarySlipBaseEmployee.__ne__(salarySlipDifferentTaxableIncome)


def test_salarySlipShouldBeNotEqualsIfTaxPayableIsDifferent(salarySlipBaseEmployee):
    salarySlipDifferentTaxPayable = getDifferentTaxPayable(getBaseEmployee())
    assert salarySlipBaseEmployee.__ne__(salarySlipDifferentTaxPayable)
