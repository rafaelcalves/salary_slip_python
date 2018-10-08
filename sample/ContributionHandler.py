from sample.Utils import Utils


class ContributionHandler:
    def __init__(self, lowerRateContribution, higherRateContribution, untaxedRoof):
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
        return Utils.getMonthlyValueFor(taxedAmount)

    def getTaxedAmountFor(self, annualGrossSalary):
        return annualGrossSalary - self.untaxedRoof

    def isTaxed(self, annualGrossSalary):
        return annualGrossSalary > self.untaxedRoof
