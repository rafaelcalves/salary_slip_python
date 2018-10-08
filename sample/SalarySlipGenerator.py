from sample.SalarySlip import SalarySlip
from sample.TaxHandler import TaxHandler
from sample.SalarySlipConstans import SalarySlipConstants
from sample.Utils import Utils


class SalarySlipGenerator:

    def __init__(self):
        self.taxHandler = TaxHandler()

    def generateFor(self, employee):
        salarySlip = SalarySlip(employee)
        salarySlip.monthlyGrossSalary = self.__calculateMonthlySalary(employee)
        self.__handleNationalInsurance(salarySlip, employee.grossSalary)
        self.__handleTaxPayable(salarySlip, employee.grossSalary)
        return salarySlip

    def __calculateMonthlySalary(self, employee):
        return Utils.getMonthlyValueFor(employee.grossSalary)

    def __handleNationalInsurance(self, salarySlip, annualGrossSalary):
        if self.taxHandler.nationalInsurance.isTaxed(annualGrossSalary):
            if self.taxHandler.isTaxedForHigherRate(annualGrossSalary):
                taxedAmount = self.taxHandler.getHigherRateTaxedAmountFor(annualGrossSalary)
                salarySlip.nationalInsurance = self.taxHandler.nationalInsurance.applyHigherRateTo(taxedAmount)
                taxedAmount = self.taxHandler.nationalInsurance.getTaxedAmountFor(SalarySlipConstants.HIGHER_RATE_ROOF)
            else:
                taxedAmount = self.taxHandler.nationalInsurance.getTaxedAmountFor(annualGrossSalary)

            salarySlip.nationalInsurance = round(salarySlip.nationalInsurance + self.taxHandler.nationalInsurance.applyLowerRateTo(taxedAmount), 2)

    def __handleTaxPayable(self, salarySlip, annualGrossSalary):
        if self.taxHandler.taxPayable.isTaxed(annualGrossSalary):
            self.applyHigherEarner(annualGrossSalary, salarySlip)
            if self.taxHandler.isTaxedForHigherRate(annualGrossSalary):
                taxedAmount = self.taxHandler.getHigherRateTaxedAmountFor(annualGrossSalary)
                salarySlip.taxPayable = salarySlip.taxPayable + self.taxHandler.taxPayable.applyHigherRateTo(taxedAmount)
                taxedAmount = self.taxHandler.taxPayable.getTaxedAmountFor(SalarySlipConstants.HIGHER_RATE_ROOF)
                self.__applyTaxPayableToSalarySlip(salarySlip, taxedAmount)
            else:
                taxedAmount = self.taxHandler.taxPayable.getTaxedAmountFor(annualGrossSalary)
                self.__applyTaxPayableToSalarySlip(salarySlip, taxedAmount)

    def applyHigherEarner(self, annualGrossSalary, salarySlip):
        if self.taxHandler.isHigherEarner(annualGrossSalary):
            self.__handleHigherEarnerExtraContribution(annualGrossSalary, salarySlip)

    def __applyTaxPayableToSalarySlip(self, salarySlip, taxedAmount):
        salarySlip.taxPayable = round(salarySlip.taxPayable + self.taxHandler.taxPayable.applyLowerRateTo(taxedAmount), 2)
        self.__applyResultantTaxPayableTaxesTo(salarySlip)

    def __applyResultantTaxPayableTaxesTo(self, salarySlip):
        monthlyUntaxedRoof = Utils.getMonthlyValueFor(SalarySlipConstants.TaxPayable.UNTAXED_ROOF)
        salarySlip.taxFreeAllowance = salarySlip.taxFreeAllowance + monthlyUntaxedRoof
        salarySlip.taxableIncome = round(salarySlip.monthlyGrossSalary - salarySlip.taxFreeAllowance, 2)

    def __handleHigherEarnerExtraContribution(self, annualGrossSalary, salarySlip):
        extraTaxedAmount = self.taxHandler.getHigherEarnerTaxedAmountFor(annualGrossSalary)
        salarySlip.taxPayable = self.taxHandler.taxPayable.applyHigherRateTo(extraTaxedAmount)
        salarySlip.taxFreeAllowance = salarySlip.taxFreeAllowance - Utils.getMonthlyValueFor(extraTaxedAmount)
