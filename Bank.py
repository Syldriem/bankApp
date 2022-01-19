from Account import Account
from Customer import Customer

class Bank:
    customerList = []
    customers = {1001: "Me", 1002: "You"}

    def _load():
        f = open("db.txt", "wt")
        a = []
        for s in Customer.customer_list:
            a.append(str(s)+ "\n")
        f.writelines(a)
        f.close()

    def get_customers(self):
        for customer in self.customerList:
            print(customer)
        

    def add_customers(self, name, pnr):
        if Customer.getPnr(pnr):
           print("didnt add")
        else:
           self.customerList.append(Customer(name, pnr))
           Bank._load()

    def get_customer(self, pnr):
        return Customer.get_customer(pnr)

    def change_customer_name(self, name, pnr):
        Customer.change_name(name, pnr)
        Bank._load()

    def remove_customer(self, pnr):
        Customer.remove_customer(pnr)
        Bank._load()
    
    def add_account(self, pnr):
           for customer in self.customerList:
               customerIndex = self.customerList.index(customer)
               if Customer.getPnr(pnr) == True:
                   self.customerList.insert(customerIndex, Account())
                   

    def get_account(self, account_id):
        return print(Account.show_acc(account_id))

    def deposit(self, account_id, amount):
        pass

    def withdraw(self, pnr, account_id, amount):
        pass

    def close_account(self, pnr, account_id):
        pass

        
    def get_all_transactions(self, pnr, acc_r):
        pass


bank = Bank()
bank.add_customers("elliot", 19980118)
bank.add_account(19980118)

bank.add_customers("axel", 19920426)

bank.add_customers("axel", 19920426)
##bank.add_account(19980118)
bank.add_customers("axel2", 199204262)

##print(Account())

bank.get_customers()
##print(Customer.customer_list[0][2])
##bank.add_account(19920426)
##print(Customer.customer_list)

##f = open("db.txt", "rt")
##newlist = []
##for line in f:
##    newlist.append(line)
##for a in newlist:
##    if "19920426" in a:
##        s = a[0:-3]
##        s += ", '1003 0 debit']]"
##       print(s)
##

print(bank.get_customer(19920426))
bank.change_customer_name("hej", 199204262)
##bank.remove_customer(199204262)
print(Customer.customer_list)
bank.get_account(1002)
