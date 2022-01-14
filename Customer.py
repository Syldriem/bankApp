from Account import Account
class Customer:
    accounts = []

    def __init__(self, name, pnr) -> None:
        self.name = name
        self.pnr = pnr
        self.accounts.append(Account())

    def __str__(self) -> str:
        stringacc = ""
        for account in self.accounts:
            stringacc += str(account)
        return f"{self.name} {self.pnr} {stringacc}"

    def getPnr(self, customer):
        for x in Customer.accounts:
            if (customer == x):
                return True
            else:
                return False