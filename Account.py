import operator

class Account:
    account_type = "debit"
    account_list = []
    account_num_list = [1000]
    
    def __init__(self, acc_nbr = 0, balance = 0) -> None:
        self.balance = balance
        if int(acc_nbr) > max(Account.account_num_list):
            self.acc_nr = acc_nbr
        else:
            self.acc_nr = max(Account.account_num_list)+1
        Account.account_num_list.append(int(self.acc_nr))
        
        Account.account_list.append([self.acc_nr, int(self.balance), self.account_type])

    def __str__(self) -> str:
        return f"{self.acc_nr} {self.balance} {self.account_type} "

        
    def get_acc_nr(self, acc_nr):
        getter = operator.attrgetter("acc_nr")
        return getter(self.account_list[acc_nr])

    def show_acc(acc_nr):
        for x in Account.account_list:
            if (str(acc_nr) == x[0]):
                return x

    def add_to_balance(account, amount):
        x = int(account.balance)
        account.balance = (x+amount)

    def take_from_balance(account, amount):
        x = int(account.balance)
        if (x-amount)>=0:
            account.balance = (x-amount)
        else:
            print("not enough money in account")


