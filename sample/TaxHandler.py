from sample.SalarySlipConstans import SalarySlipConstants
from sample.ContributionHandler import ContributionHandler


class TaxHandler:

    def __init__(self):
        self.nationalInsurance = ContributionHandler(SalarySlipConstants.NationalInsurance.LOWER_RATE_CONTRIBUTION,
                                                     SalarySlipConstants.NationalInsurance.HIGHER_RATE_CONTRIBUTION,
                                                     SalarySlipConstants.NationalInsurance.UNTAXED_ROOF)
        self.taxPayable = ContributionHandler(SalarySlipConstants.TaxPayable.LOWER_RATE_CONTRIBUTION,
                                              SalarySlipConstants.TaxPayable.HIGHER_RATE_CONTRIBUTION,
                                              SalarySlipConstants.TaxPayable.UNTAXED_ROOF)

    @classmethod
    def getHigherRateTaxedAmountFor(cls, annualGrossSalary):
        return annualGrossSalary - SalarySlipConstants.HIGHER_RATE_ROOF

    @classmethod
    def getHigherEarnerTaxedAmountFor(cls, annualGrossSalary):
        limitedValue = cls.__limitValueForHigherEarnersTaxes(annualGrossSalary)
        return (limitedValue - SalarySlipConstants.HigherEarner.RATE_ROOF) / 2

    @classmethod
    def __limitValueForHigherEarnersTaxes(cls, annualGrossSalary):
        if annualGrossSalary > SalarySlipConstants.HigherEarner.EXTRA_BASE_LIMIT:
            return SalarySlipConstants.HigherEarner.EXTRA_BASE_LIMIT
        return annualGrossSalary

    @classmethod
    def isTaxedForHigherRate(cls, annualGrossSalary):
        return annualGrossSalary > SalarySlipConstants.HIGHER_RATE_ROOF

    @classmethod
    def isHigherEarner(cls, annualGrossSalary):
        return annualGrossSalary > SalarySlipConstants.HigherEarner.RATE_ROOF
