

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



    def conn(self, path):
        try:
            open(path, "rt")
            return (True, "Connection successful", path)
        except:
            return (False, "Connection unsuccessful")

    def get_all(path):
        Datasource.datasource_list = []
        f = open(path, "rt")
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

    def update_trans(list):
        f = open(Datasource.transaction_path, "wt")
        a = []
        for s in list:
            a.append(str(s)+ "\n")
        f.writelines(a)
        f.close()