from sample.Contribution import Contribution


class HigherEarnerContribution(Contribution):

    def __init__(self, untaxedRoof, extraBaseLimit):
        super().__init__(untaxedRoof)
        self.extraBaseLimit = extraBaseLimit

    def getTaxedAmountFor(self, annualGrossSalary):
        limitedValue = self.__limitValueForHigherEarnersTaxes(annualGrossSalary)
        return (limitedValue - self.untaxedRoof) / 2

    def __limitValueForHigherEarnersTaxes(self, annualGrossSalary):
        if annualGrossSalary > self.extraBaseLimit:
            return self.extraBaseLimit
        return annualGrossSalary
