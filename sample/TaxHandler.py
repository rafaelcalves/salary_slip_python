from sample.SalarySlipConstans import SalarySlipConstants


class TaxHandler:
    @classmethod
    def applyNationalInsuranceLowerRateToAmount(cls, amount):
        return cls.__applyTaxToAmount(amount, SalarySlipConstants.NationalInsurance.LOWER_RATE_CONTRIBUTION)

    @classmethod
    def applyTaxPayableLowerRateToAmount(cls, amount):
        return cls.__applyTaxToAmount(amount, SalarySlipConstants.TaxPayable.LOWER_RATE_CONTRIBUTION)

    @classmethod
    def applyNationalInsuranceHigherRateToAmount(cls, amount):
        return cls.__applyTaxToAmount(amount, SalarySlipConstants.NationalInsurance.HIGHER_RATE_CONTRIBUTION)

    @classmethod
    def applyTaxPayableHigherRateToAmount(cls, amount):
        return cls.__applyTaxToAmount(amount, SalarySlipConstants.TaxPayable.HIGHER_RATE_CONTRIBUTION)

    @classmethod
    def __applyTaxToAmount(cls, amount, tax):
        taxedAmount = amount * tax
        return cls.getMonthlyValueFor(taxedAmount)

    @classmethod
    def getMonthlyValueFor(cls, value):
        return round(value / SalarySlipConstants.MONTHS, 2)

    @classmethod
    def getTaxPayableTaxedAmountFor(cls, annualGrossSalary):
        return annualGrossSalary - SalarySlipConstants.TaxPayable.UNTAXED_ROOF

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
    def isTaxedForTaxPayable(cls, annualGrossSalary):
        return annualGrossSalary > SalarySlipConstants.TaxPayable.UNTAXED_ROOF

    @classmethod
    def isTaxedForNationalInsurance(cls, annualGrossSalary):
        return annualGrossSalary > SalarySlipConstants.NationalInsurance.UNTAXED_ROOF

    @classmethod
    def isTaxedForHigherRate(cls, annualGrossSalary):
        return annualGrossSalary > SalarySlipConstants.HIGHER_RATE_ROOF

    @classmethod
    def isHigherEarner(cls, annualGrossSalary):
        return annualGrossSalary > SalarySlipConstants.HigherEarner.RATE_ROOF

    @classmethod
    def getNationalInsuranceTaxedAmountFor(cls, annualGrossSalary):
        return annualGrossSalary - SalarySlipConstants.NationalInsurance.UNTAXED_ROOF
