from asyncio.windows_events import NULL
from math import radians
from re import A
from unicodedata import name
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
            i = 5
            index = 1
            while index <= (len(x)-5)/3:
                Bank.add_account(x[1],x[i], x[i+1])
                i += 3
                index +=1

    
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
        getter = operator.attrgetter("pnr", "name")
        for customer in Bank.customerList:
            print(getter(customer))


    def add_customers(name, pnr, *args):
        if Bank.checkPnr(pnr):
           return print(f"{name} didnt add"), False
        elif len(str(pnr)) == 8:
            if len(args) == 0:
                Bank.customerList.append(Customer(name, pnr))
                Bank._load()
            else:
                Bank.customerList.append(Customer(name, pnr, args[0], args[1]))
                Bank._load()
        else:
            return print("wrong length person number"), False

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
        
        for x in Bank.customerList:
            temp_index = Bank.customerList.index(x)
            if str(pnr) == getter(bank.customerList[temp_index]):
                customer = Bank.customerList[temp_index]
                Customer.change_name2(customer, name)
                Bank._load()
                return print(f"name changed to {name}"), True
            
        print("no person with that id number")
                

    def remove_customer(self, pnr):
        getter = operator.attrgetter("pnr")
        getter2 = operator.attrgetter("accounts")
        getter3 = operator.attrgetter("balance")
        for x in Bank.customerList:
            temp_index = Bank.customerList.index(x)
            if str(pnr) == getter(bank.customerList[temp_index]):
                accounts = getter2(Bank.customerList[temp_index])
                deleted_cust = []
                account_balance = 0
                for x in accounts:
                    account_balance += int(getter3(x))

                for x in Account.get_acc(accounts):
                    deleted_cust.append(Bank.close_account(x))
                del Bank.customerList[temp_index]
                Bank._load()
                return print(f"customer removed. These accounts deleted:\
{deleted_cust} {account_balance}:- has been returned") 
            
        print("no person with that id number")
    
    def add_account(pnr, acc_nb, balance):
        getter = operator.attrgetter("pnr")
        
        for x in Bank.customerList:
            temp_index = Bank.customerList.index(x)
            if str(pnr) == getter(Bank.customerList[temp_index]):
                customer = Bank.customerList[temp_index]
                Customer.add_account(customer, acc_nb, balance)
                Bank._load()
                return print("account added")
            
        print("no person with that id number")
        
    

    def get_account(self, account_id):
        getter = operator.attrgetter("acc_nr")
        for x in Customer.account_list:
            temp_index = Customer.account_list.index(x)
            if str(account_id) == getter(Customer.account_list[temp_index]):
                account = Customer.account_list[temp_index]
                print(account)



    def deposit(account_id, amount):
        getter = operator.attrgetter("acc_nr")
        
        for x in Customer.account_list:
            temp_index = Customer.account_list.index(x)
            if str(account_id) == getter(Customer.account_list[temp_index]):
                account = Customer.account_list[temp_index]
                Account.add_to_balance(account, amount)
                Bank._load()
                return print("Money deposited")
            
        print("no account with that id number")
        
    def checkPnr(pnr):
        getter = operator.attrgetter("pnr")
        for x in Bank.customerList:
            temp_index = Bank.customerList.index(x)
            if str(pnr) == getter(Bank.customerList[temp_index]):
                return True
        return False


    def withdraw(account_id, amount):
        getter = operator.attrgetter("acc_nr")
        
        for x in Customer.account_list:
            temp_index = Customer.account_list.index(x)
            if str(account_id) == getter(Customer.account_list[temp_index]):
                account = Customer.account_list[temp_index]
                Account.take_from_balance(account, amount)
                Bank._load()
                return print("Money withdrawn")
            
        print("no account with that id number")

    def close_account(account_id):
        getter = operator.attrgetter("acc_nr")
        
        for x in Customer.account_list:
            temp_index = Customer.account_list.index(x)
            if str(account_id) == getter(Customer.account_list[temp_index]):
                account = Customer.account_list[temp_index]
                del Customer.account_list[temp_index]

                getter2 = operator.attrgetter("accounts")
                for x in Bank.customerList:
                    temp_index = Bank.customerList.index(x)
                    if account in getter2(Bank.customerList[temp_index]):
                        customer = Bank.customerList[temp_index]
                        
                        Customer.delete_account_from_cust(customer, account)
                        Bank._load()
                        print(f"Account deleted with id: {account_id}")
                        return str(account)


                
            
        print("no account with that id number")

        
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


bank.change_customer_name("elliot2", 19980118)
#getter2 = operator.attrgetter("name")
##print(getter2(Bank.customerList[0]))

##bank.add_account(19920426)


##bank.remove_customer(19920426)
##print(Bank.customerList)

##Bank.deposit(1004, 30)
##Bank.withdraw(1001, 30)
##Bank.close_account(1001)
Bank.add_customers("sten", 19920412)
#Bank.add_account(19980118, 1020, 100)
bank.get_customers()
bank.get_account(1001)
bank.get_customer(19980118)

