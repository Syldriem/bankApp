import operator

from Account import Account
from Customer import Customer
from Datasource import Datasource
from Transaction import Transaction


class Bank:
    customerList = []

    def __init__(self):
        Transaction.get_transactions()
        temp_list = Datasource.get_all("db.txt")
        for line in temp_list:
            x = line.split()
            Bank.add_customers(x[1], x[2], x[4], x[3], x[0])
            i = 6
            index = 1
            while index <= (len(x)-6)/3:
                Bank.add_account(x[2],x[i+1], x[i])
                i += 3
                index +=1


    def _load():
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
                Customer.change_name(customer, name)
                Bank._load()
                return print(f"name changed to {name}"), True
            
        print("no person with that id number")
        return False
                

    def remove_customer(pnr):
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
                    acc_nr = Customer.add_account(customer, balance)
                else:
                    acc_nr = Customer.add_account(customer, balance, args[0])
                Bank._load()
                return acc_nr
            
        print("no person with that id number")
        return -1
        
    

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
                return True
            
        return False
        
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
                                del Bank.customerList[temp_index2]
                                Customer.remove_customer(Bank.customerList[temp_index2])
                                Bank._load()
                                print("last account removed, customer deleted")
                                return str(account)
                            else:
                                customer = Bank.customerList[temp_index2]
                                del Customer.account_list[temp_index1]
                                Customer.delete_account_from_cust(customer, account)
                                Bank._load()
                                print(f"Account deleted with id: {account_id} and {balance}:- is returned")
                                return str(account)
        print("no account with that id number")

                
            


        
    def get_transactions_from_acc(acc_nr):
        getter = operator.attrgetter("account_id")
        temp_str = ""
        for x in Transaction.trans_record:
            temp_index = Transaction.trans_record.index(x)
            if str(acc_nr) == getter(Transaction.trans_record[temp_index]):
                transaction = Transaction.trans_record[temp_index]
                temp_str += Transaction.get_transaction_from_acc(transaction)
            
        if temp_str == "":
            return -1
        else:
            return print(f"account: {acc_nr} has transactions: {temp_str}")
        
