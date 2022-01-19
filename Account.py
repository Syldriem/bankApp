


class Account:
    acc_nr = 1001
    account_type = "debit"
    account_list = []
    def __init__(self, balance = 0) -> None:
        self.balance = balance
        self.acc_nr = Account.acc_nr
        Account.acc_nr += 1
        Account.account_list.append([self.acc_nr, int(self.balance), self.account_type])

    def __str__(self) -> str:
        return f"{self.acc_nr} {self.balance} {self.account_type}"

        
    def get_acc_nr(self):
        pass

    def show_acc(acc_nr):
        for x in Account.account_list:
            if (acc_nr in x):
                return x

    ##ef add_to_balance(acc_nr, amount):
        ##Customer.account_list[acc_nr] += amount

    def take_from_balance(self, acc_nr, amount):
        pass
