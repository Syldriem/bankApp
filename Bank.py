from Account import Account
from Customer import Customer

class Bank:
    customerList = []
    customers = {1001: "Me", 1002: "You"}

    def _load(self):
        pass

    def get_customers(self):
        for customer in self.customerList:
            print(customer)
        

    def add_customers(self, name, pnr):
        self.name = name
        for customer in self.customerList:
            if Customer.getPnr(customer):
                print("didnt add")
            else:
                return self.customerList.append(Customer(name, pnr))

        
    def get_customer(self, pnr):
        return self.customerList.index(pnr)

    def change_customer_name(self, name, pnr):
        pass

    def remove_customer(self, pnr):
        pass

    def add_account(self, pnr):
        pass

    def get_account(self, pnr, account_id):
        pass

    def deposit(self, pnr, account_id, amount):
        pass

    def withdraw(self, pnr, account_id, amount):
        pass

    def close_account(self, pnr, account_id):
        pass

        
    def get_all_transactions(self, pnr, acc_r):
        pass


bank = Bank()
bank.add_customers("elliot", 19980118)

bank.add_customers("axel", 19920426)


bank.add_customers("axel", 19920426)

print(Account())

bank.get_customers()
