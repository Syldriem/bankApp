import operator
from Account import Account

class Customer:
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


    def __str__(self) -> str:
        stringacc = ""
        for account in self.accounts:
            stringacc += str(account)
        return f"{self.name} {self.pnr} {stringacc}"




    def cust_from_list(name, pnr, account_id, balance):
        return Customer(name, pnr, account_id, balance)



    def add_account(customer, acc_num, balance):
        a = Account(acc_num, balance)
        customer.accounts.append(a)
        customer.account_list.append(a)
        
        

    def remove_customer(customer):
        del customer




    def change_name2(customer, name):
        customer.name = name



    def delete_account_from_cust(customer, account):
        temp_index = customer.accounts
        for x in customer.accounts:
            temp_index = customer.accounts.index(x)
            if account == x:
                del customer.accounts[temp_index]
