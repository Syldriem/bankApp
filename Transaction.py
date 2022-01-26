
from datetime import date
from Datasource import Datasource

class Transaction:

    trans_id = 1
    trans_record = []
    def __init__(self, customer_id, account_id, amount) -> None:
            
        self.customer_id = customer_id
        self.account_id = account_id
        self.date = date.today()
        self.amount = amount
        Transaction.trans_record.append(self)

        f = open("dbtransaction.txt", "wt")
        a = []
        for s in Transaction.trans_record:
            a.append(str(s)+ "\n")
        f.writelines(a)
        f.close()

    def __str__(self):
        return f"{self.customer_id}, {self.account_id}, {self.date}, {self.amount} "
