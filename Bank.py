from asyncio.windows_events import NULL
from math import radians
from Account import Account
from Customer import Customer
import operator

class Bank:
    customerList = []

    def __init__(self):
        temp_list = []
        f = open("db.txt", "rt")
        for line in f:
            temp_list.append(line)
        f.close()
        for line in temp_list:
            x = line.split()
            print(x)
            Bank.add_customers(x[0], x[1], x[2], x[3])
            ##Bank.update_customers(x[0], x[1], x[2], x[3])
            if len(x)>=6:
                Bank.add_account(x[1],x[5], x[6])
    
    ##def update_customers(name, pnr, account_id, account_balance):
    ##    Bank.customerList.append(Customer.cust_from_list(name, pnr, account_id, account_balance))
        


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
        

    def add_customers(name, pnr, acc_num, balance):
        if Customer.getPnr(pnr):
           print("didnt add")
        elif len(str(pnr)) == 8:
           Bank.customerList.append(Customer(name, pnr, acc_num, balance))
           Bank._load()
        else:
            print("wrong length person number")

    def get_customer(self, pnr):
        getter = operator.attrgetter("pnr")
        for x in Bank.customerList:
            temp_index = Bank.customerList.index(x)
            if str(pnr) == getter(bank.customerList[temp_index]):
                customer = Bank.customerList[temp_index]
                return print(customer)

        print("no person with that id number")

    def change_customer_name(self, name, pnr):
        getter = operator.attrgetter("pnr")
        
        temp_index = Bank.customerList.index
        for x in Bank.customerList:
            temp_index = Bank.customerList.index(x)
            if str(pnr) == getter(bank.customerList[temp_index]):
                customer = Bank.customerList[temp_index]
                Customer.change_name2(customer, name)
                Bank._load()
                return print("name changed")
            
        print("no person with that id number")
                

    def remove_customer(self, pnr):
        getter = operator.attrgetter("pnr")
        
        temp_index = Bank.customerList.index
        for x in Bank.customerList:
            temp_index = Bank.customerList.index(x)
            if str(pnr) == getter(bank.customerList[temp_index]):
                customer = Bank.customerList[temp_index]
                ##Customer.remove_customer(customer)
                del Bank.customerList[temp_index]
                Bank._load()
                return print("customer removed")
            
        print("no person with that id number")
    
    def add_account(pnr, acc_nb, balance):
        getter = operator.attrgetter("pnr")
        
        temp_index = Bank.customerList.index
        for x in Bank.customerList:
            temp_index = Bank.customerList.index(x)
            print(pnr)
            asd = getter(Bank.customerList[temp_index])
            print(asd)
            if str(pnr) == getter(Bank.customerList[temp_index]):
                customer = Bank.customerList[temp_index]
                Customer.add_account(customer, acc_nb, balance)
                Bank._load()
                return print("account added")
            
        print("no person with that id number")
        
    

    def get_account(self, account_id):
        print(Account.show_acc(account_id))

    def deposit(self, pnr, account_id, amount):

        Customer.account_list[pnr][account_id] += amount


    def withdraw(self, pnr, account_id, amount):
        pass

    def close_account(self, pnr, account_id):
        pass

        
    def get_all_transactions(self, pnr, acc_r):
        pass

##    newlist = []
##    def add_acc(self, pnr):
##        f = open("db.txt", "rt")
##        acc_nr = bank.get_account(Account().acc_nr)
##        i = str(acc_nr)[1:]
##        for line in f:
##            self.newlist.append(line)
##        for a in self.newlist:
##            if str(pnr) in a:
##                s = a[0:-3]
##                s += f", {i}]\n"
##                self.newlist[self.newlist.index(a)] = s
##                f.close()
##        f = open("db.txt", "wt")
##      f.writelines(self.newlist)      
##        f.close() 
##        self.newlist = []
##        Customer.update_customer_list()


bank = Bank()
##bank.add_customers("elliot", 19980118)

##bank.add_customers("axel", 19920426)

##bank.add_customers("axel", 19920426)
##bank.add_account(19980118)
##bank.add_customers("axel2", 19920427)

##print(Account())

##bank.get_customers()
##print(Customer.customer_list[0][2])
##bank.add_account(19920426)
##print(Customer.customer_list)



##print(bank.get_customer(19920426))
##bank.change_customer_name("hej", 199204262)
##bank.remove_customer(199204262)
##print(Customer.customer_list)
##bank.get_account(1002)
##print(bank.deposit(1001, 50))
##bank.add_acc(19920426)

##bank.add_acc(19980118)


##bank.remove_customer(19920426)



##print(Customer.customer_list)
##print(Account.account_list)
##print(bank.get_account(1001))
##print(bank.customerList)


##print(getter(bank.customerList[0]))
##print(type(bank.customerList[0]))
##print(Bank.customerList)
##print(getter(bank.customerList[0]))

##print(getter(bank.customerList[1]))
##print(getter2(Customer.account_list[0]))
##print(Customer.account_list)
##bank.deposit(19920426, 1002, 50)
bank.change_customer_name("elliot2", 19980118)
#getter2 = operator.attrgetter("name")
##print(getter2(Bank.customerList[0]))

##bank.add_account(19920426)

print(Customer.customer_list)
##bank.remove_customer(19920426)
print(Bank.customerList)
print(Account.account_list)
bank.get_customers()