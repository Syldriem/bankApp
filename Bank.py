import operator
from asyncio.windows_events import NULL
from math import radians
from re import A
from unicodedata import name

from Account import Account
from Customer import Customer
from Datasource import Datasource


class Bank:
    customerList = []

    def __init__(self):
        temp_list = Datasource.get_all()
        for line in temp_list:
            x = line.split()
            Bank.add_customers(x[1], x[2], x[4], x[3], x[0])
            ##Bank.update_customers(x[0], x[1], x[2], x[3])
            i = 6
            index = 1
            while index <= (len(x)-6)/3:
                Bank.add_account(x[2],x[i+1], x[i])
                i += 3
                index +=1

    
    ##def update_customers(name, pnr, account_id, account_balance):
    ##    Bank.customerList.append(Customer.cust_from_list(name, pnr, account_id, account_balance))
        


    def _load():
        ##f = open("db.txt", "wt")
        ##a = []
        ##for s in Bank.customerList:
        ##    a.append(str(s)+ "\n")
        ##f.writelines(a)
        ##f.close()
        Datasource.update_db(Bank.customerList)


    def get_customers():
        getter = operator.attrgetter("pnr", "name")
        for customer in Bank.customerList:
            print(getter(customer))


    def add_customers(name, pnr, *args):
        if Bank.checkPnr(pnr):
           return print(f"{name} didnt add, customer with that ssn already exists"), False
        elif len(str(pnr)) == 8:
            if len(args) == 0:
                Bank.customerList.append(Customer(name, pnr))
                Bank._load()
                return True
            else:
                Bank.customerList.append(Customer(name, pnr, args[0], args[1], args[2]))
                Bank._load()
                return True
        else:
            return print("wrong length person number"), False

    def get_customer(self, pnr):
        getter = operator.attrgetter("pnr")
        for x in Bank.customerList:
            temp_index = Bank.customerList.index(x)
            if str(pnr) == getter(Bank.customerList[temp_index]):
                customer = Bank.customerList[temp_index]
                return print(customer)

        print("no person with that id number")

    def change_customer_name(self, name, pnr):
        getter = operator.attrgetter("pnr")
        
        for x in Bank.customerList:
            temp_index = Bank.customerList.index(x)
            if str(pnr) == getter(Bank.customerList[temp_index]):
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
            if str(pnr) == getter(Bank.customerList[temp_index]):
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
    
    def add_account(pnr, balance, *args):
        getter = operator.attrgetter("pnr")
        
        for x in Bank.customerList:
            temp_index = Bank.customerList.index(x)
            if str(pnr) == getter(Bank.customerList[temp_index]):
                customer = Bank.customerList[temp_index]
                if len(args) == 0:
                    Customer.add_account(customer, balance)
                else:
                    Customer.add_account(customer, balance, args[0])
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



    def deposit(pnr, account_id, amount):
        getter = operator.attrgetter("acc_nr")
        
        for x in Customer.account_list:
            temp_index = Customer.account_list.index(x)
            if str(account_id) == getter(Customer.account_list[temp_index]):
                account = Customer.account_list[temp_index]
                Account.add_to_balance(pnr, account, amount)
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
                status = Account.take_from_balance(account, amount)
                Bank._load()
                return status
            
        print("no account with that id number")

    def close_account(account_id):
        getter = operator.attrgetter("acc_nr")
        getter3 = operator.attrgetter("balance")
        
        for x in Customer.account_list:
            temp_index1 = Customer.account_list.index(x)
            if str(account_id) == getter(Customer.account_list[temp_index1]):
                    account = Customer.account_list[temp_index1]
                    balance = getter3(Customer.account_list[temp_index1])
                    

                    getter2 = operator.attrgetter("accounts")
                    for x in Bank.customerList:
                        temp_index2 = Bank.customerList.index(x)
                        if account in getter2(Bank.customerList[temp_index2]):
                            if len(getter2(Bank.customerList[temp_index2])) == 1:
                                print("Customer only has one account, cant delete")
                                return str(account)
                            else:
                                customer = Bank.customerList[temp_index2]
                                del Customer.account_list[temp_index1]
                                Customer.delete_account_from_cust(customer, account)
                                Bank._load()
                                print(f"Account deleted with id: {account_id} and {balance}:- is returned")
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


##bank.add_customers("elliot", 19980118)

##bank.add_customers("axel", 19920426)

##bank.add_customers("axel", 19920426)
##bank.add_account(19980118)
##bank.add_customers("axel2", 19920427)


#getter2 = operator.attrgetter("name")
##print(getter2(Bank.customerList[0]))

##bank.add_account(19920426)


##bank.remove_customer(19920426)
##print(Bank.customerList)

##Bank.deposit(1004, 30)
##Bank.withdraw(1001, 30)
##Bank.close_account(1001)
#Bank.add_account(19980118, 1020, 100)
##bank = Bank()
##print(Customer.account_list)
##print(Bank.withdraw(1001, 60))
