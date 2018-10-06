from sample.SalarySlip import SalarySlip

MONTHS = 12

UNTAXED_TAX_PAYABLE_ROOF = 11000
TAX_PAYABLE_CONTRIBUTION = .2

UNTAXED_NATIONAL_INSURANCE_ROOF = 8060
NATIONAL_INSURANCE_CONTRIBUTION = .12



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
        return cls.__getMonthlyValueFor(employee.grossSalary)

    @classmethod
    def __calculateNationalInsurance(cls, annualGrossSalary):
        if annualGrossSalary > UNTAXED_NATIONAL_INSURANCE_ROOF:
            taxedAmount = annualGrossSalary - UNTAXED_NATIONAL_INSURANCE_ROOF
            return cls.__applyNationalInsuranceToAmount(taxedAmount)
        else:
            return 0

    @classmethod
    def __handleTaxPayable(cls, salarySlip, annualGrossSalary):
        if annualGrossSalary > UNTAXED_TAX_PAYABLE_ROOF:
            taxedAmount = annualGrossSalary - UNTAXED_TAX_PAYABLE_ROOF
            salarySlip.taxPayable = cls.__applyTaxPayableToAmount(taxedAmount)
            salarySlip.taxFreeAllowance = cls.__getMonthlyValueFor(UNTAXED_TAX_PAYABLE_ROOF)
            salarySlip.taxableIncome = round(salarySlip.monthlyGrossSalary - salarySlip.taxFreeAllowance, 2)

    @classmethod
    def __applyNationalInsuranceToAmount(cls, amount):
        return cls.__applyTaxToAmount(amount, NATIONAL_INSURANCE_CONTRIBUTION)

    @classmethod
    def __applyTaxPayableToAmount(cls, amount):
        return cls.__applyTaxToAmount(amount, TAX_PAYABLE_CONTRIBUTION)

    @classmethod
    def __applyTaxToAmount(cls, amount, tax):
        taxedAmount = amount * tax
        return cls.__getMonthlyValueFor(taxedAmount)

    @classmethod
    def __getMonthlyValueFor(cls, value):
        return round(value / MONTHS, 2)
