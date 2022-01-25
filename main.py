from msilib.schema import MsiAssemblyName

from pip import main
from Account import Account
from Customer import Customer
from Bank import Bank

bank = Bank()
customer_options = {
    "1": "See customer information",
    "2": "Deposit to customer account",
    "3": "Withdraw from customer account",
    "4": "Print a list of customers",
    "5": "Add a customer",
    "6": "Change customer name",
    "7": "Remove a customer",
    "8": "Add account to customer",
    "9": "Remove account from customer",
    "10": "Exit"
}

while True:
    for x in customer_options:

        print(x, ":", customer_options[x])
    options = input("Enter number to select option: ")

    if options == "1":
        pnr = input("Social security number: ")
        if Bank.checkPnr(pnr) == False:
            print("No customer with this number")
        else:
            bank.get_customer(pnr)
        input("Press enter to return to menu")

    elif options == "2":
        try:
            account_id = input("Account id: ")
            amount = int(input("Amount: "))
            Bank.deposit(account_id, amount)
            input("Press enter to return to menu")
        except:
            print("ERROR: enter a number")
            input("Press enter to return to menu")

    elif options == "3":
        try:
            account_id = input("Account id: ")
            amount = int(input("Amount: "))
            Bank.withdraw(account_id, amount)
            input("Press enter to return to menu")
        except:
            print("ERROR: enter a number")
            input("Press enter to return to menu")
    elif options == "4":
        Bank.get_customers()
        input("Press enter to return to menu")

    elif options == "5":
        name = input("Name: ")
        pnr = input("Social security number: ")
        Bank.add_customers(name, pnr)
        input("Press enter to return to menu")

    elif options == "6":
        name = input("New name: ")
        pnr = input("Social security number: ")
        bank.change_customer_name(name, pnr)
        input("Press enter to return to menu")

    elif options == "7":
        pnr = input("Social security number: ")
        bank.remove_customer(pnr)
        input("Press enter to return to menu")

    elif options == "8":
        pnr = input("Social security number: ") 
        amount = input("Enter starting amount: ")
        Bank.add_account(pnr, amount)
        input("Press enter to return to menu")

    elif options == "9":
        account_id = input("Account id: ")
        Bank.close_account(account_id)
        input("Press enter to return to menu")

    elif options == "10":
        exit()

