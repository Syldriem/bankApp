from Account import Account
class Customer:
    customer_list = []

    def __init__(self, name, pnr) -> None:
        self.accounts = []
        self.name = name
        self.pnr = pnr
        self.accounts.append(Account())
        Customer.customer_list.append([self.pnr, self.name, self.accounts])

    def __str__(self) -> str:
        stringacc = ""
        for account in self.accounts:
            stringacc += str(account)
        return f"{self.name} {self.pnr} {stringacc}"

    def getPnr(pnr):
        for x in Customer.customer_list:
            if (pnr in x):
                return True
        return False   
    
    def add_Account(self, pnr):
        self.pnr = pnr
        if Customer.getPnr(pnr):
            for x in Customer.customer_list:
                for c in x:
                    if c == pnr:
                       self.accounts.append(Account())


        else:
            print("didn't add account")