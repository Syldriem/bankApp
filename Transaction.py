
from datetime import datetime

from Datasource import Datasource


class Transaction:

    trans_id_list = []
    trans_record = []
    def __init__(self, customer_id, account_id, amount, trans_id=1, date=None) -> None:
        if int(trans_id) not in Transaction.trans_id_list:
            self.trans_id = str(trans_id)
        else:
            self.trans_id = str(max(Transaction.trans_id_list)+1)
        Transaction.trans_id_list.append(int(self.trans_id))
        self.customer_id = customer_id
        self.account_id = account_id
        if date == None:
            self.date = datetime.now().replace(microsecond=0).isoformat()
        else:
            self.date = date
        self.amount = amount
        Transaction.trans_record.append(self)

        Datasource.update_trans(Transaction.trans_record)

    def __str__(self):
        return f"{self.trans_id} {self.customer_id} {self.account_id} {self.date} {self.amount} "

    def get_transactions():
        temp_list = Datasource.get_all("dbtransaction.txt")
        for line in temp_list:
            x = line.split()
            Transaction(x[1],x[2],x[4],x[0],x[3])

    def get_transaction_from_acc(transaction):
        trans_date = str(transaction.date).replace("T", " ")
        trans_amount = transaction.amount
        return f"Date: {trans_date} Amount: {trans_amount}; "
