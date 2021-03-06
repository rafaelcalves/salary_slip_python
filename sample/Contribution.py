from sample.MonthsHandler import MonthsHandler


class Contribution:
    def __init__(self, untaxedRoof, lowerRateContribution=0, higherRateContribution=0):
        self.lowerRateContribution = lowerRateContribution
        self.higherRateContribution = higherRateContribution
        self.untaxedRoof = untaxedRoof

    def applyLowerRateTo(self, amount):
        return self.__applyTaxToAmount(amount, self.lowerRateContribution)

    def applyHigherRateTo(self, amount):
        return self.__applyTaxToAmount(amount, self.higherRateContribution)

    @staticmethod
    def __applyTaxToAmount(amount, tax):
        taxedAmount = amount * tax
        return MonthsHandler.getMonthlyValueFor(taxedAmount)

    def getTaxedAmountFor(self, annualGrossSalary):
        return annualGrossSalary - self.untaxedRoof

    def isTaxed(self, annualGrossSalary):
        return annualGrossSalary > self.untaxedRoof
