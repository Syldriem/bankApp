from Account import Account


class Customer:
    """Customer class. Here we have functions to manipulate a customer"""
    account_list = []
    customer_id_list = [111110]
    def __init__(self, name, pnr, *args) -> None:
        """Initializes the customer with attributes"""
        self.accounts = []
        self.name = name
        self.pnr = pnr
        if len(args) == 0:
            self.customer_id = max(Customer.customer_id_list)+1
        else:
            if args[2] not in Customer.customer_id_list:
                self.customer_id = str(args[2])
            else:
                self.customer_id = max(Customer.customer_id_list)+1
        Customer.customer_id_list.append(int(self.customer_id))

        if len(args) == 0:
            a = Account(self.pnr)
        else:
            a = Account(self.pnr, args[0], args[1])
        self.accounts.append(a)
        Customer.account_list.append(a)


    def __str__(self) -> str:
        """Stringifies a customer and their accounts"""
        stringacc = ""
        for account in self.accounts:
            stringacc += str(account)
        return f"{self.customer_id} {self.name} {self.pnr} {stringacc}"




    def add_account(customer, balance, *args):
        """Adds an account to a customer and a list of all accounts"""
        if len(args) == 0:
            a = Account(customer.pnr, balance)
        else:
        
            a = Account(customer.pnr, balance, args[0])
        customer.accounts.append(a)
        customer.account_list.append(a)
        return a.acc_nr
        
        

    def remove_customer(customer):
        """Deletes a customer"""
        del customer




    def change_name(customer, name):
        """Changes a customer's name"""
        customer.name = name



    def delete_account_from_cust(customer, account):
        """Deletes an account from a customer"""
        temp_index = customer.accounts
        for x in customer.accounts:
            temp_index = customer.accounts.index(x)
            if account == x:
                del customer.accounts[temp_index]
