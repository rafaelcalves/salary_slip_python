import pytest

from sample.Employee import Employee
from sample.SalarySlip import SalarySlip
from sample.SalarySlipGenerator import SalarySlipGenerator


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


def test_salarySlipShouldBeEqualsToSalarySlipAnnualSalary5000():
    employee = getEmployeeAnnualSalary5000()
    salarySlip = SalarySlipGenerator.generateFor(employee)
    expectedSalarySlip = getSalarySlipAnnualSalary5000(employee)
    assert salarySlip.__eq__(expectedSalarySlip)


def test_salarySlipShouldBeEqualsToSalarySlipAnnualSalary9060():
    employee = getEmployeeAnnualSalary9060()
    salarySlip = SalarySlipGenerator.generateFor(employee)
    expectedSalarySlip = getSalarySlipAnnualSalary9060(employee)
    assert salarySlip.__eq__(expectedSalarySlip)


def test_salarySlipShouldBeEqualsToSalarySlipAnnualSalary12000():
    employee = getEmployeeAnnualSalary12000()
    salarySlip = SalarySlipGenerator.generateFor(employee)
    expectedSalarySlip = getSalarySlipAnnualSalary12000(employee)
    assert salarySlip.__eq__(expectedSalarySlip)


def test_salarySlipShouldBeEqualsToSalarySlipAnnualSalary45000():
    employee = getEmployeeAnnualSalary45000()
    salarySlip = SalarySlipGenerator.generateFor(employee)
    expectedSalarySlip = getSalarySlipAnnualSalary45000(employee)
    assert salarySlip.__eq__(expectedSalarySlip)


def test_salaeySlipShouldBeEqualsToSalarySlipAnnualSalary101000():
    employee = getEmployeeAnnualSalary101000()
    salarySlip = SalarySlipGenerator.generateFor(employee)
    expectedSalarySlip = getSalarySlipAnnualSalary101000(employee)
    assert salarySlip.__eq__(expectedSalarySlip)


def test_salaeySlipShouldBeEqualsToSalarySlipAnnualSalary150000():
    employee = getEmployeeAnnualSalary150000()
    salarySlip = SalarySlipGenerator.generateFor(employee)
    expectedSalarySlip = getSalarySlipAnnualSalary150000(employee)
    assert salarySlip.__eq__(expectedSalarySlip)
