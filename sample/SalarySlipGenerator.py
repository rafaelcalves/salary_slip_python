from sample.SalarySlip import SalarySlip
from sample.TaxHandler import TaxHandler
from sample.SalarySlipConstans import SalarySlipConstants

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
        natinonalInsurance = 0
        if TaxHandler.isTaxedForNationalInsurance(annualGrossSalary):
            if TaxHandler.isTaxedForHigherRate(annualGrossSalary):
                taxedAmount = TaxHandler.getHigherRateTaxedAmountFor(annualGrossSalary)
                natinonalInsurance = TaxHandler.applyNationalInsuranceHigherRateToAmount(taxedAmount)
                taxedAmount = TaxHandler.getNationalInsuranceTaxedAmountFor(SalarySlipConstants.HIGHER_RATE_ROOF)
            else:
                taxedAmount = TaxHandler.getNationalInsuranceTaxedAmountFor(annualGrossSalary)

            natinonalInsurance = round(
                natinonalInsurance + TaxHandler.applyNationalInsuranceLowerRateToAmount(taxedAmount), 2)
        return natinonalInsurance

    @classmethod
    def __handleTaxPayable(cls, salarySlip, annualGrossSalary):
        if TaxHandler.isTaxedForTaxPayable(annualGrossSalary):
            if TaxHandler.isHigherEarner(annualGrossSalary):
                cls.__handleHigherEarnerExtraContribution(annualGrossSalary, salarySlip)
            if TaxHandler.isTaxedForHigherRate(annualGrossSalary):
                taxedAmount = TaxHandler.getHigherRateTaxedAmountFor(annualGrossSalary)
                salarySlip.taxPayable = salarySlip.taxPayable + TaxHandler.applyTaxPayableHigherRateToAmount(
                    taxedAmount)
                taxedAmount = TaxHandler.getTaxPayableTaxedAmountFor(SalarySlipConstants.HIGHER_RATE_ROOF)
                cls.__applyTaxPayableToSalarySlip(salarySlip, taxedAmount)
            else:
                taxedAmount = TaxHandler.getTaxPayableTaxedAmountFor(annualGrossSalary)
                cls.__applyTaxPayableToSalarySlip(salarySlip, taxedAmount)

    @classmethod
    def __applyTaxPayableToSalarySlip(cls, salarySlip, taxedAmount):
        salarySlip.taxPayable = salarySlip.taxPayable + TaxHandler.applyTaxPayableLowerRateToAmount(taxedAmount)
        cls.__applyResultantTaxPayableTaxesTo(salarySlip)

    @classmethod
    def __applyResultantTaxPayableTaxesTo(cls, salarySlip):
        monthlyUntaxedRoof = TaxHandler.getMonthlyValueFor(SalarySlipConstants.TaxPayable.UNTAXED_ROOF)
        salarySlip.taxFreeAllowance = salarySlip.taxFreeAllowance + monthlyUntaxedRoof
        salarySlip.taxableIncome = round(salarySlip.monthlyGrossSalary - salarySlip.taxFreeAllowance, 2)

    @classmethod
    def __handleHigherEarnerExtraContribution(cls, annualGrossSalary, salarySlip):
        extraTaxedAmount = TaxHandler.getHigherEarnerTaxedAmountFor(annualGrossSalary)
        salarySlip.taxPayable = TaxHandler.applyTaxPayableHigherRateToAmount(extraTaxedAmount)
        salarySlip.taxFreeAllowance = salarySlip.taxFreeAllowance - TaxHandler.getMonthlyValueFor(extraTaxedAmount)
