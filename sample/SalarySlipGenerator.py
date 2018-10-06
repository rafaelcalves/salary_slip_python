from sample.SalarySlip import SalarySlip

class SalarySlipGenerator:
    @staticmethod
    def generateFor(employee):
        return SalarySlip(employee, employee.grossSalary/12)
