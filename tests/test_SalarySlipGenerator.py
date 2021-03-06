import pytest

from sample.tuples.Employee import Employee
from sample.tuples.SalarySlip import SalarySlip
from sample.SalarySlipGenerator import SalarySlipGenerator


@pytest.fixture(autouse=True)
def salarySlipGenerator():
    return SalarySlipGenerator()


# iteration 1


def getEmployeeAnnualSalary5000():
    return Employee(12345, "John J Doe", 5000)


def getSalarySlipAnnualSalary5000(employee):
    return SalarySlip(employee, 416.67)


# iteration 2


def getEmployeeAnnualSalary9060():
    return Employee(12345, "John J Doe", 9060)


def getSalarySlipAnnualSalary9060(employee):
    return SalarySlip(employee, 755, 10)


# iteration 3


def getEmployeeAnnualSalary12000():
    return Employee(12345, "John J Doe", 12000)


def getSalarySlipAnnualSalary12000(employee):
    return SalarySlip(employee, 1000, 39.40, 916.67, 83.33, 16.67)


# iteration 4


def getEmployeeAnnualSalary45000():
    return Employee(12345, "John J Doe", 45000)


def getSalarySlipAnnualSalary45000(employee):
    return SalarySlip(employee, 3750, 352.73, 916.67, 2833.33, 600)


# iteration 5


def getEmployeeAnnualSalary101000():
    return Employee(12345, "John J Doe", 101000)


def getSalarySlipAnnualSalary101000(employee):
    return SalarySlip(employee, 8416.67, 446.07, 875.00, 7541.67, 2483.33)


def getEmployeeAnnualSalary150000():
    return Employee(12345, "John J Doe", 150000)


def getSalarySlipAnnualSalary150000(employee):
    return SalarySlip(employee, 12500, 527.73, 0, 12500, 4466.67)


# iteration 6


def getEmployeeAnnualSalary160000():
    return Employee(12345, "John J Doe", 160000)


def getSalarySlipAnnualSalary160000(employee):
    return SalarySlip(employee, 13333.33, 544.40, 0, 13333.33, 4841.67)


def test_salarySlipShouldBeEqualsToSalarySlipAnnualSalary5000(salarySlipGenerator):
    employee = getEmployeeAnnualSalary5000()
    salarySlip = salarySlipGenerator.generateFor(employee)
    expectedSalarySlip = getSalarySlipAnnualSalary5000(employee)
    assert salarySlip.__eq__(expectedSalarySlip)


def test_salarySlipShouldBeEqualsToSalarySlipAnnualSalary9060(salarySlipGenerator):
    employee = getEmployeeAnnualSalary9060()
    salarySlip = salarySlipGenerator.generateFor(employee)
    expectedSalarySlip = getSalarySlipAnnualSalary9060(employee)
    assert salarySlip.__eq__(expectedSalarySlip)


def test_salarySlipShouldBeEqualsToSalarySlipAnnualSalary12000(salarySlipGenerator):
    employee = getEmployeeAnnualSalary12000()
    salarySlip = salarySlipGenerator.generateFor(employee)
    expectedSalarySlip = getSalarySlipAnnualSalary12000(employee)
    assert salarySlip.__eq__(expectedSalarySlip)


def test_salarySlipShouldBeEqualsToSalarySlipAnnualSalary45000(salarySlipGenerator):
    employee = getEmployeeAnnualSalary45000()
    salarySlip = salarySlipGenerator.generateFor(employee)
    expectedSalarySlip = getSalarySlipAnnualSalary45000(employee)
    assert salarySlip.__eq__(expectedSalarySlip)


def test_salaeySlipShouldBeEqualsToSalarySlipAnnualSalary101000(salarySlipGenerator):
    employee = getEmployeeAnnualSalary101000()
    salarySlip = salarySlipGenerator.generateFor(employee)
    expectedSalarySlip = getSalarySlipAnnualSalary101000(employee)
    assert salarySlip.__eq__(expectedSalarySlip)


def test_salaeySlipShouldBeEqualsToSalarySlipAnnualSalary150000(salarySlipGenerator):
    employee = getEmployeeAnnualSalary150000()
    salarySlip = salarySlipGenerator.generateFor(employee)
    expectedSalarySlip = getSalarySlipAnnualSalary150000(employee)
    assert salarySlip.__eq__(expectedSalarySlip)


def test_salaeySlipShouldBeEqualsToSalarySlipAnnualSalary160000(salarySlipGenerator):
    employee = getEmployeeAnnualSalary160000()
    salarySlip = salarySlipGenerator.generateFor(employee)
    expectedSalarySlip = getSalarySlipAnnualSalary160000(employee)
    assert salarySlip.__eq__(expectedSalarySlip)
