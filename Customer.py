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
            self.account_numb.append(a)
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
        pass

    def get_customer(pnr):
        for x in Customer.customer_list:
            if (pnr in x):
                return x
        return "no such user"
    
    def change_name(name, pnr):
        for x in Customer.customer_list:
            if (pnr in x):
                x[1] = name
                print(Customer.customer_list)
    
    def remove_customer(pnr):
        for x in Customer.customer_list:
            if (pnr in x):
                Customer.customer_list.remove(x)
                print(Customer.customer_list)
                
