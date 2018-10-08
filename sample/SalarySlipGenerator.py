from sample.Constans import SalarySlipConstants
from sample.ContributionsHandler import ContributionsHandler
from sample.MonthsHandler import MonthsHandler
from sample.tuples.SalarySlip import SalarySlip


class SalarySlipGenerator:

    def __init__(self):
        self.contributionsHandler = ContributionsHandler()

    def generateFor(self, employee):
        salarySlip = SalarySlip(employee)
        salarySlip.monthlyGrossSalary = self.__calculateMonthlySalary(employee)
        self.__handleNationalInsurance(salarySlip, employee.grossSalary)
        self.__handleTaxPayable(salarySlip, employee.grossSalary)
        return salarySlip

    def __calculateMonthlySalary(self, employee):
        return MonthsHandler.getMonthlyValueFor(employee.grossSalary)

    def __handleNationalInsurance(self, salarySlip, annualGrossSalary):
        if self.contributionsHandler.nationalInsurance.isTaxed(annualGrossSalary):
            if self.contributionsHandler.higherRate.isTaxed(annualGrossSalary):
                taxedAmount = self.contributionsHandler.higherRate.getTaxedAmountFor(annualGrossSalary)
                salarySlip.nationalInsurance = self.contributionsHandler.nationalInsurance.applyHigherRateTo(
                    taxedAmount)
                taxedAmount = self.contributionsHandler.nationalInsurance.getTaxedAmountFor(
                    SalarySlipConstants.HIGHER_RATE_ROOF)
            else:
                taxedAmount = self.contributionsHandler.nationalInsurance.getTaxedAmountFor(annualGrossSalary)

            salarySlip.nationalInsurance = round(
                salarySlip.nationalInsurance + self.contributionsHandler.nationalInsurance.applyLowerRateTo(
                    taxedAmount), 2)

    def __handleTaxPayable(self, salarySlip, annualGrossSalary):
        if self.contributionsHandler.taxPayable.isTaxed(annualGrossSalary):
            self.applyHigherEarner(annualGrossSalary, salarySlip)
            if self.contributionsHandler.aditionalRate.isTaxed(annualGrossSalary):
                taxedAmount = self.contributionsHandler.aditionalRate.getTaxedAmountFor(annualGrossSalary)
                salarySlip.taxPayable = salarySlip.taxPayable + self.contributionsHandler.aditionalRate.applyLowerRateTo(
                    taxedAmount)
                annualGrossSalary = SalarySlipConstants.AditionalRate.RATE_ROOF
            if self.contributionsHandler.higherRate.isTaxed(annualGrossSalary):
                taxedAmount = self.contributionsHandler.higherRate.getTaxedAmountFor(annualGrossSalary)
                salarySlip.taxPayable = salarySlip.taxPayable + self.contributionsHandler.taxPayable.applyHigherRateTo(
                    taxedAmount)
                taxedAmount = self.contributionsHandler.taxPayable.getTaxedAmountFor(
                    SalarySlipConstants.HIGHER_RATE_ROOF)
                self.__applyTaxPayableToSalarySlip(salarySlip, taxedAmount)
            else:
                taxedAmount = self.contributionsHandler.taxPayable.getTaxedAmountFor(annualGrossSalary)
                self.__applyTaxPayableToSalarySlip(salarySlip, taxedAmount)

    def applyHigherEarner(self, annualGrossSalary, salarySlip):
        if self.contributionsHandler.higherEarner.isTaxed(annualGrossSalary):
            self.__handleHigherEarnerExtraContribution(annualGrossSalary, salarySlip)

    def __applyTaxPayableToSalarySlip(self, salarySlip, taxedAmount):
        salarySlip.taxPayable = round(
            salarySlip.taxPayable + self.contributionsHandler.taxPayable.applyLowerRateTo(taxedAmount), 2)
        self.__applyResultantTaxPayableTaxesTo(salarySlip)

    def __applyResultantTaxPayableTaxesTo(self, salarySlip):
        monthlyUntaxedRoof = MonthsHandler.getMonthlyValueFor(SalarySlipConstants.TaxPayable.UNTAXED_ROOF)
        salarySlip.taxFreeAllowance = salarySlip.taxFreeAllowance + monthlyUntaxedRoof
        salarySlip.taxableIncome = round(salarySlip.monthlyGrossSalary - salarySlip.taxFreeAllowance, 2)

    def __handleHigherEarnerExtraContribution(self, annualGrossSalary, salarySlip):
        extraTaxedAmount = self.contributionsHandler.higherEarner.getTaxedAmountFor(annualGrossSalary)
        salarySlip.taxPayable = self.contributionsHandler.taxPayable.applyHigherRateTo(extraTaxedAmount)
        salarySlip.taxFreeAllowance = salarySlip.taxFreeAllowance - MonthsHandler.getMonthlyValueFor(extraTaxedAmount)
