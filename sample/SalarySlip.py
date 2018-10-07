class SalarySlip:
    def __init__(self, employee, monthlyGrossSalary=0, nationalInsurance=0, taxFreeAllowance=0, taxableIncome=0, taxPayable=0):
        self.employee = employee
        self.monthlyGrossSalary = monthlyGrossSalary
        self.nationalInsurance = nationalInsurance
        self.taxFreeAllowance = taxFreeAllowance
        self.taxableIncome = taxableIncome
        self.taxPayable = taxPayable

    def __eq__(self, object):
        if isinstance(object, SalarySlip):
            if object.monthlyGrossSalary == self.monthlyGrossSalary \
                and object.nationalInsurance == self.nationalInsurance \
                and object.taxFreeAllowance == self.taxFreeAllowance \
                and object.taxableIncome ==  self.taxableIncome \
                and object.taxPayable == self.taxPayable:
                return True
        return False

    def __ne__(self, object):
        return not self.__eq__()
