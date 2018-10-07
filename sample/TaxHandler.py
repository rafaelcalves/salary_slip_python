MONTHS = 12

TAX_PAYABLE_CONTRIBUTION_LOWER_RATE = .2
TAX_PAYABLE_CONTRIBUTION_HIGHER_RATE = .4

NATIONAL_INSURANCE_CONTRIBUTION_LOWER_RATE = .12
NATIONAL_INSURANCE_CONTRIBUTION_HIGHER_RATE = .02

UNTAXED_TAX_PAYABLE_ROOF = 11000
UNTAXED_NATIONAL_INSURANCE_ROOF = 8060
HIGHER_RATE_ROOF = 43000

class TaxHandler:
    @classmethod
    def applyNationalInsuranceLowerRateToAmount(cls, amount):
        return cls.__applyTaxToAmount(amount, NATIONAL_INSURANCE_CONTRIBUTION_LOWER_RATE)

    @classmethod
    def applyTaxPayableLowerRateToAmount(cls, amount):
        return cls.__applyTaxToAmount(amount, TAX_PAYABLE_CONTRIBUTION_LOWER_RATE)

    @classmethod
    def applyNationalInsuranceHigherRateToAmount(cls, amount):
        return cls.__applyTaxToAmount(amount, NATIONAL_INSURANCE_CONTRIBUTION_HIGHER_RATE)

    @classmethod
    def applyTaxPayableHigherRateToAmount(cls, amount):
        return cls.__applyTaxToAmount(amount, TAX_PAYABLE_CONTRIBUTION_HIGHER_RATE)

    @classmethod
    def __applyTaxToAmount(cls, amount, tax):
        taxedAmount = amount * tax
        return cls.getMonthlyValueFor(taxedAmount)

    @classmethod
    def getMonthlyValueFor(cls, value):
        return round(value / MONTHS, 2)