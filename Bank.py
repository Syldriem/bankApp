from Account import Account
from Customer import Customer

class Bank:
    customerList = []
    customers = {1001: "Me", 1002: "You"}
    newlist = []

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
        elif len(str(pnr)) == 8:
           self.customerList.append(Customer(name, pnr))
           Bank._load()
        else:
            print("wrong length person number")

    def get_customer(self, pnr):
        return Customer.get_customer(pnr)

    def change_customer_name(self, name, pnr):
        Customer.change_name(name, pnr)
        Bank._load()

    def remove_customer(self, pnr):
        Customer.remove_customer(pnr)
        Bank._load()
    
    def add_account(self, pnr):
        Customer.add_account(pnr, Account().acc_nr)
        
    

    def get_account(self, account_id):
        return Account.show_acc(account_id)

    def deposit(self, account_id, amount):
        return Account.add_to_balance(account_id, amount)


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

##print(Account())

bank.get_customers()
##print(Customer.customer_list[0][2])
##bank.add_account(19920426)
##print(Customer.customer_list)



print(bank.get_customer(19920426))
bank.change_customer_name("hej", 199204262)
##bank.remove_customer(199204262)
print(Customer.customer_list)
bank.get_account(1002)
print(bank.deposit(1001, 50))
bank.add_acc(19920426)

bank.add_acc(19980118)


bank.remove_customer(19920426)
print(Customer.customer_list)