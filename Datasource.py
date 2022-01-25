

class Datasource:
    datasource_list = []
    customer_path = ""
    transaction_path = ""
    def __init__(self, t_path="dbtransaction.txt", c_path="db.txt") -> None:
        self.transaction_path = t_path
        self.customer_path = c_path
        Datasource.customer_path = c_path
        Datasource.transaction_path = t_path
        print(self.conn(self.transaction_path))
        print(self.conn(self.customer_path))
        ##self.load_transactions()
        ##self.get_all()


    def conn(self, path):
        test_data = path.split(".")
        if test_data[1] == "txt":
            return (True, "Connection successful", path)
        else:
            return (False, "Connection unsuccessful")

    def get_all():
        f = open("db.txt", "rt")
        for line in f:
            Datasource.datasource_list.append(line)
        f.close()
        return Datasource.datasource_list

    def update_db(list):
        f = open(Datasource.customer_path, "wt")
        a = []
        for s in list:
            a.append(str(s)+ "\n")
        f.writelines(a)
        f.close()

    def update_by_id():
        pass
    def remove_by_id():
        pass

##db = Datasource()
