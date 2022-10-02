"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contractType, contractHours, contractPay, commissionType, contractsLanded, commissionPay):
        self.name = name
        self.commission = Commission(commissionType, contractsLanded, commissionPay)
        self.contract = Contract(contractType, contractHours, contractPay)

    def get_pay(self):
        return self.contract.contractPayment() + self.commission.commissionPayment()

    def __str__(self):
        self.contractString = self.contract.contractString()
        self.commissionString = self.commission.commissionString()
        return f"{self.name} works on a {self.contractString}{self.commissionString}.  Their total pay is {self.get_pay()}."

class Contract:
    def __init__(self, contractType, contractHours, contractPay):
        self.contractType = contractType
        self.contractHours = contractHours
        self.contractPay = contractPay

    def contractPayment(self):
        if self.contractType == "hourly":
            return self.contractHours * self.contractPay
        else:
            return self.contractPay

    def contractString(self):
        if self.contractType == "hourly":
            return f"contract of {self.contractHours} hours at {self.contractPay}/hour"
        else:
            return f"monthly salary of {self.contractPay}"

class Commission:
    def __init__(self, commissionType, contractsLanded, commissionPay):
        self.commissionType = commissionType
        self.contractsLanded = contractsLanded
        self.commissionPay = commissionPay

    def commissionPayment(self):
        if self.commissionType == None:
            return 0
        elif self.commissionType == "bonus":
            return self.commissionPay
        else:
            return self.commissionPay * self.contractsLanded

    def commissionString(self):
        if self.commissionType == "bonus":
            return f" and receives a bonus commission of {self.commissionPay}"
        elif self.commissionType == "variable":
            return f" and receives a commission for {self.contractsLanded} contract(s) at {self.commissionPay}/contract"
        else:
            return ""

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "monthly", None, 4000, None, None, None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "hourly", 100, 25, None, None, None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "monthly", None, 3000, "variable", 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "hourly", 150, 25, "variable", 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "monthly", None, 2000, "bonus", None, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "hourly", 120, 30, "bonus", None, 600)
