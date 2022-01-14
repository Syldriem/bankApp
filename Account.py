class Account:
    acc_nr = 1001
    account_type = "debit"
    account_list = []
    def __init__(self, balance = 0) -> None:
        self.balance = balance
        self.acc_nr = Account.acc_nr
        Account.acc_nr += 1
        Account.account_list.append([self.acc_nr, self.balance, self.account_type])

    def __str__(self) -> str:
        return f"{self.acc_nr} {self.balance} {self.account_type}"

        
    def get_acc_nr(self):
        pass

    def show_acc(self, acc_nr):
        pass

    def add_to_balance(self, acc_nr, amount):
        pass

    def take_from_balance(self, acc_nr, amount):
        pass

    
