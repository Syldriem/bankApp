from Account import Account
class Customer:
    customer_list = []

    def __init__(self, name, pnr) -> None:
        self.accounts = []
        self.name = name
        self.pnr = pnr
        self.accounts.append(Account())
        self.account_numb = []
        for account in self.accounts:
            a = str(account)
            self.account_numb.append(a[0:4])
        Customer.customer_list.append([self.pnr, self.name, self.account_numb])

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

    def add_account(pnr, account_number):
        i = 0
        for x in Customer.customer_list:
            if (pnr in x):
                
        i += 1
