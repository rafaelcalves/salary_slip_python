from sample.SalarySlipConstans import SalarySlipConstants
from sample.Contribution import Contribution
from sample.HigherEarnerContribution import HigherEarnerContribution


class ContributionsHandler:

    def __init__(self):
        self.nationalInsurance = Contribution(SalarySlipConstants.NationalInsurance.UNTAXED_ROOF,
                                              SalarySlipConstants.NationalInsurance.LOWER_RATE_CONTRIBUTION,
                                              SalarySlipConstants.NationalInsurance.HIGHER_RATE_CONTRIBUTION)
        self.taxPayable = Contribution(SalarySlipConstants.TaxPayable.UNTAXED_ROOF,
                                       SalarySlipConstants.TaxPayable.LOWER_RATE_CONTRIBUTION,
                                       SalarySlipConstants.TaxPayable.HIGHER_RATE_CONTRIBUTION)
        self.higherRate = Contribution(SalarySlipConstants.HIGHER_RATE_ROOF)
        self.higherEarner = HigherEarnerContribution(SalarySlipConstants.HigherEarner.RATE_ROOF,
                                                     SalarySlipConstants.HigherEarner.EXTRA_BASE_LIMIT)
        self.aditionalRate = Contribution(SalarySlipConstants.AditionalRate.RATE_ROOF,
                                          SalarySlipConstants.AditionalRate.CONTRIBUTION)
