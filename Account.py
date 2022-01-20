

class Account:
    acc_nr = 1001
    account_type = "debit"
    account_list = []
    def __init__(self, acc_nbr = acc_nr, balance = 0) -> None:

        self.balance = balance
        self.acc_nr = acc_nbr
        ##self.acc_nr = args
        Account.acc_nr += 1
        Account.account_list.append([self.acc_nr, int(self.balance), self.account_type])

    def __str__(self) -> str:
        return f"{self.acc_nr} {self.balance} {self.account_type} "

        
    def get_acc_nr(self):
        pass

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


