from Account import Account


class Customer:
    
    account_list = []
    customer_id = [111110]
    def __init__(self, name, pnr, *args) -> None:
        self.accounts = []
        self.name = name
        self.pnr = pnr
        if len(args) == 0:
            self.customer_id = max(Customer.customer_id)+1
        else:
            if args[2] not in Customer.customer_id:
                self.customer_id = args[2]
            else:
                self.customer_id = max(Customer.customer_id_list)+1
        Customer.customer_id_list.append(int(self.customer_id))

        if len(args) == 0:
            a = Account(self.pnr)
        else:
            a = Account(self.pnr, args[0], args[1])
        self.accounts.append(a)
        self.account_list.append(a)


    def __str__(self) -> str:
        stringacc = ""
        for account in self.accounts:
            stringacc += str(account)
        return f"{self.customer_id} {self.name} {self.pnr} {stringacc}"




    def add_account(customer, balance, *args):
        if len(args) == 0:
            a = Account(customer.pnr, balance)
        else:
        
            a = Account(customer.pnr, balance, args[0])
        customer.accounts.append(a)
        customer.account_list.append(a)
        return a.acc_nr
        
        

    def remove_customer(customer):
        del customer




    def change_name(customer, name):
        customer.name = name



    def delete_account_from_cust(customer, account):
        temp_index = customer.accounts
        for x in customer.accounts:
            temp_index = customer.accounts.index(x)
            if account == x:
                del customer.accounts[temp_index]
