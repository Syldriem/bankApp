import operator
from Account import Account
"""Hej detta är en modul"""

class Customer:
    ## FIX CUSTOMER ID INT##
    account_list = []
    customer_id_list = [111110]
    def __init__(self, name, pnr, *args) -> None:
        self.accounts = []
        if len(args) == 0:
            self.customer_id = max(Customer.customer_id_list)+1
        else:
            if args[2] not in Customer.customer_id_list:
                self.customer_id = str(args[2])
            else:
                asd = max(Customer.customer_id_list)+1
                self.customer_id = str(asd)

        Customer.customer_id_list.append(int(self.customer_id))
        self.name = name
        self.pnr = pnr
        if len(args) == 0:
            a = Account()
        else:
            a = Account(args[0], args[1])
        self.accounts.append(a)
        Customer.account_list.append(a)


    def __str__(self) -> str:
        stringacc = ""
        for account in self.accounts:
            stringacc += str(account)
        return f"{self.customer_id} {self.name} {self.pnr} {stringacc}"




    def cust_from_list(name, pnr, account_id, balance):
        return Customer(name, pnr, account_id, balance)



    def add_account(customer, balance, *args):
        if len(args) == 0:
            a = Account(balance)
        else:
        
            a = Account(balance, args[0])
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
