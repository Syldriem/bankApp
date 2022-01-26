

from Bank import Bank
from Datasource import Datasource

db = Datasource()
bank = Bank()

bank_options = {
    "1": "See customer information",
    "2": "Deposit to customer account",
    "3": "Withdraw from customer account",
    "4": "Print a list of customers",
    "5": "Add a customer",
    "6": "Change customer name",
    "7": "Remove a customer",
    "8": "Add account to customer",
    "9": "Remove account from customer",
    "10": "Get transactions from account",
    "11": "Exit"
}

while True:
    for x in bank_options:

        print(x, ":", bank_options[x])
    options = input("Enter number to select option: ")

    if options == "1":
        pnr = input("Social security number: ")
        print("------------------------------")
        if Bank.checkPnr(pnr) == False:
            print("No customer with this number")
        else:
            bank.get_customer(pnr)
        
        print("------------------------------")
        input("Press enter to return to menu")
        print("------------------------------")

    elif options == "2":
        try:
            account_id = input("Account id: ")
            amount = int(input("Amount to deposit: "))
            print("------------------------------")
            if Bank.deposit(account_id, amount) == True:
                print("Money deposited")
            else:
                print("no account with that id number")
            
        except:
            print("ERROR: enter a number")
        
        print("------------------------------")
        input("Press enter to return to menu")
        print("------------------------------")    
    elif options == "3":
        try:
            account_id = input("Account id: ")
            amount = int(input("Amount to withdraw: "))
            print("------------------------------")
            Bank.withdraw(account_id, amount)
            
        except:
            print("ERROR: enter a number")
            
        print("------------------------------")
        input("Press enter to return to menu")
        print("------------------------------")     
    elif options == "4":
        print("------------------------------")
        Bank.get_customers()
        print("------------------------------")
        input("Press enter to return to menu")
        print("------------------------------") 

    elif options == "5":
        name = input("Name: ")
        pnr = input("Social security number: ")
        print("------------------------------")
        if Bank.add_customers(name, pnr) == True:
            print("Customer added")
        print("------------------------------")
        input("Press enter to return to menu")
        print("------------------------------") 

    elif options == "6":
        name = input("New name: ")
        pnr = input("Social security number: ")
        print("------------------------------")
        bank.change_customer_name(name, pnr)
        print("------------------------------")
        input("Press enter to return to menu")
        print("------------------------------") 

    elif options == "7":
        pnr = input("Social security number: ")
        print("------------------------------")
        Bank.remove_customer(pnr)
        print("------------------------------")
        input("Press enter to return to menu")
        print("------------------------------") 


    elif options == "8":
        pnr = input("Social security number: ") 
        amount = input("Enter starting amount: ")
        print("------------------------------")
        acc_nr = Bank.add_account(pnr, amount)
        if acc_nr != -1:
            print(f"account added with number {acc_nr}")
        print("------------------------------")
        input("Press enter to return to menu")
        print("------------------------------") 


    elif options == "9":
        account_id = input("Account id: ")
        print("------------------------------")
        Bank.close_account(account_id)
        print("------------------------------")
        input("Press enter to return to menu")
        print("------------------------------") 

    elif options == "10":
        account_id = input("account id: ")
        if Bank.get_transactions_from_acc(account_id) == -1:
            print("account doesnt exist")
        
        print("------------------------------")
        input("Press enter to return to menu")
        print("------------------------------") 

    elif options == "11":
        exit()

