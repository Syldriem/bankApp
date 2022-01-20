from Account import Account
class Customer:
    customer_list = []
    account_list = []
    def __init__(self, name, pnr, *args) -> None:
        self.accounts = []
        self.name = name
        self.pnr = pnr
        if len(args) == 0:
            a = Account()
        else:
            a = Account(args[0], args[1])
        self.accounts.append(a)
        self.account_list.append(a)
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

    def cust_from_list(name, pnr, account_id, balance):
        return Customer(name, pnr, account_id, balance)

    def getPnr(pnr):
        for x in Customer.customer_list:
            if (pnr in x):
                return True
        return False

    def add_account(customer, acc_num, balance):
        a = Account(acc_num, balance)
        customer.accounts.append(a)
        customer.account_list.append(a)
        
        

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
    
    def remove_customer(customer):
        del customer

    def update_customer_list():
        Customer.customer_list = []
        f = open("db.txt", "rt")
        for line in f:
            Customer.customer_list.append(line.rstrip("\n"))
        f.close()

    def change_name2(customer, name):
        print(customer.name)
        customer.name = name

    def delete_account_from_cust(customer, account):
        temp_index = customer.accounts
        for x in customer.accounts:
            temp_index = customer.accounts.index(x)
            if account == x:
                del customer.accounts[temp_index]
