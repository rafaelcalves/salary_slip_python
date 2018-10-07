from sample.SalarySlip import SalarySlip
from sample.TaxHandler import TaxHandler


UNTAXED_TAX_PAYABLE_ROOF = 11000
UNTAXED_NATIONAL_INSURANCE_ROOF = 8060
HIGHER_RATE_ROOF = 43000


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
        if cls.isTaxedForNationalInsurance(annualGrossSalary):
            natinonalInsurance = 0
            if cls.isTaxedForHigherRate(annualGrossSalary):
                taxedAmount = annualGrossSalary - HIGHER_RATE_ROOF
                natinonalInsurance = TaxHandler.applyNationalInsuranceHigherRateToAmount(taxedAmount)
                annualGrossSalary = HIGHER_RATE_ROOF
            taxedAmount = annualGrossSalary - UNTAXED_NATIONAL_INSURANCE_ROOF
            natinonalInsurance = round(natinonalInsurance + TaxHandler.applyNationalInsuranceLowerRateToAmount(taxedAmount), 2)
            return natinonalInsurance
        else:
            return 0

    @classmethod
    def __handleTaxPayable(cls, salarySlip, annualGrossSalary):
        if cls.isTaxedForTaxPayable(annualGrossSalary):
            if annualGrossSalary > 100000:
                salarySlip.taxPayable = TaxHandler.applyTaxPayableHigherRateToAmount((annualGrossSalary - 100000)/2)
                salarySlip.taxFreeAllowance = -TaxHandler.getMonthlyValueFor((annualGrossSalary - 100000)/2)
            if cls.isTaxedForHigherRate(annualGrossSalary):
                taxedAmount = annualGrossSalary - HIGHER_RATE_ROOF
                salarySlip.taxPayable = salarySlip.taxPayable + TaxHandler.applyTaxPayableHigherRateToAmount(taxedAmount)
                annualGrossSalary = HIGHER_RATE_ROOF
            taxedAmount = annualGrossSalary - UNTAXED_TAX_PAYABLE_ROOF
            salarySlip.taxPayable = salarySlip.taxPayable + TaxHandler.applyTaxPayableLowerRateToAmount(taxedAmount)
            salarySlip.taxFreeAllowance = salarySlip.taxFreeAllowance + TaxHandler.getMonthlyValueFor(UNTAXED_TAX_PAYABLE_ROOF)
            salarySlip.taxableIncome = round(salarySlip.monthlyGrossSalary - salarySlip.taxFreeAllowance, 2)

    @classmethod
    def isTaxedForTaxPayable(cls, annualGrossSalary):
        return annualGrossSalary > UNTAXED_TAX_PAYABLE_ROOF

    @classmethod
    def isTaxedForNationalInsurance(cls, annualGrossSalary):
        return annualGrossSalary > UNTAXED_NATIONAL_INSURANCE_ROOF

    @classmethod
    def isTaxedForHigherRate(cls, annualGrossSalary):
        return annualGrossSalary > HIGHER_RATE_ROOF
