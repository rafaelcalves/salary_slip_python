from sample.Constans import SalarySlipConstants


class MonthsHandler:

    @classmethod
    def getMonthlyValueFor(cls, value):
        return round(value / SalarySlipConstants.MONTHS, 2)
