from sample.SalarySlipConstans import SalarySlipConstants


class Utils:

    @classmethod
    def getMonthlyValueFor(cls, value):
        return round(value / SalarySlipConstants.MONTHS, 2)