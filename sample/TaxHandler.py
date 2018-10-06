MONTHS = 12
TAX_PAYABLE_CONTRIBUTION = .2
NATIONAL_INSURANCE_CONTRIBUTION = .12


class TaxHandler:
    @classmethod
    def applyNationalInsuranceToAmount(cls, amount):
        return cls.__applyTaxToAmount(amount, NATIONAL_INSURANCE_CONTRIBUTION)

    @classmethod
    def applyTaxPayableToAmount(cls, amount):
        return cls.__applyTaxToAmount(amount, TAX_PAYABLE_CONTRIBUTION)

    @classmethod
    def __applyTaxToAmount(cls, amount, tax):
        taxedAmount = amount * tax
        return cls.getMonthlyValueFor(taxedAmount)

    @classmethod
    def getMonthlyValueFor(cls, value):
        return round(value / MONTHS, 2)