from sample.SalarySlip import SalarySlip
from sample.TaxHandler import TaxHandler

MONTHS = 12
UNTAXED_TAX_PAYABLE_ROOF = 11000
UNTAXED_NATIONAL_INSURANCE_ROOF = 8060


class SalarySlipGenerator:
    @classmethod
    def generateFor(cls, employee):
        salarySlip = SalarySlip(employee)
        salarySlip.monthlyGrossSalary = cls.__calculateMonthlySalary(employee)
        salarySlip.nationalInsurance = cls.__calculateNationalInsurance(employee.grossSalary)
        cls.__handleTaxPayable(salarySlip, employee.grossSalary)
        return salarySlip

    @classmethod
    def __calculateMonthlySalary(cls, employee):
        return TaxHandler.getMonthlyValueFor(employee.grossSalary)

    @classmethod
    def __calculateNationalInsurance(cls, annualGrossSalary):
        if annualGrossSalary > UNTAXED_NATIONAL_INSURANCE_ROOF:
            taxedAmount = annualGrossSalary - UNTAXED_NATIONAL_INSURANCE_ROOF
            return TaxHandler.applyNationalInsuranceToAmount(taxedAmount)
        else:
            return 0

    @classmethod
    def __handleTaxPayable(cls, salarySlip, annualGrossSalary):
        if annualGrossSalary > UNTAXED_TAX_PAYABLE_ROOF:
            taxedAmount = annualGrossSalary - UNTAXED_TAX_PAYABLE_ROOF
            salarySlip.taxPayable = TaxHandler.applyTaxPayableToAmount(taxedAmount)
            salarySlip.taxFreeAllowance = TaxHandler.getMonthlyValueFor(UNTAXED_TAX_PAYABLE_ROOF)
            salarySlip.taxableIncome = round(salarySlip.monthlyGrossSalary - salarySlip.taxFreeAllowance, 2)
