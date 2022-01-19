from math import radians
from Account import Account
from Customer import Customer
import operator

class Bank:
    customerList = []
    customers = {1001: "Me", 1002: "You"}
    newlist = []

    def _load():
        f = open("db.txt", "wt")
        a = []
        for s in Bank.customerList:
            a.append(str(s)+ "\n")
        f.writelines(a)
        f.close()

    def get_customers(self):
        for customer in self.customerList:
            print(customer)
        

    def add_customers(self, name, pnr):
        if Customer.getPnr(pnr):
           print("didnt add")
        elif len(str(pnr)) == 8:
           self.customerList.append(Customer(name, pnr))
           Bank._load()
        else:
            print("wrong length person number")

    def get_customer(self, pnr):
        return Customer.get_customer(pnr)

    def change_customer_name(self, name, pnr):
        getter = operator.attrgetter("pnr")
        
        temp_index = Bank.customerList.index
        for x in Bank.customerList:
            temp_index = Bank.customerList.index(x)
            if pnr == getter(bank.customerList[temp_index]):
                customer = bank.customerList[temp_index]
                Customer.change_name2(customer, name)
                Bank._load()
                return print("name changed")
            
        print("no person with that id number")
                

    def remove_customer(self, pnr):
        Customer.remove_customer(pnr)
        ##Bank._load()
    
    def add_account(self, pnr):
        getter = operator.attrgetter("pnr")

        for x in Bank.customerList:
            temp_index = Bank.customerList.index(x)
            if pnr == getter(Bank.customerList[temp_index]):
                customer = Bank.customerList[temp_index]
                Customer.add_account(customer)
                Bank._load()
                return print("account added")
            
        print("no person with that id number")

                   

    def get_account(self, account_id):
        return Account.show_acc(account_id)

    def deposit(self, pnr, account_id, amount):

        Customer.account_list[pnr][account_id] += amount


    def withdraw(self, pnr, account_id, amount):
        pass

    def close_account(self, pnr, account_id):
        pass

        
    def get_all_transactions(self, pnr, acc_r):
        pass
    
    def add_acc(self, pnr):
        f = open("db.txt", "rt")
        acc_nr = bank.get_account(Account().acc_nr)
        i = str(acc_nr)[1:]
        for line in f:
            self.newlist.append(line)
        for a in self.newlist:
            if str(pnr) in a:
                s = a[0:-3]
                s += f", {i}]\n"
                self.newlist[self.newlist.index(a)] = s
                f.close()
        f = open("db.txt", "wt")
        f.writelines(self.newlist)      
        f.close() 
        self.newlist = []
        Customer.update_customer_list()


bank = Bank()
bank.add_customers("elliot", 19980118)


bank.add_customers("axel", 19920426)

bank.add_customers("axel", 19920426)
##bank.add_account(19980118)
bank.add_customers("axel2", 19920427)

print(Account.get_acc_nr(1001))

bank.change_customer_name("elliot2", 19980118)
getter2 = operator.attrgetter("name")
print(getter2(Bank.customerList[0]))

