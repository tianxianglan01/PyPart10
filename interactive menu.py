from small_town_teller import Bank, Person, Account

class Menu:
    def __init__(self):
        self.bank = Bank()

    def interactive_term(self):
        while True:
            choice = int(input('Welcome to the Bank Menu. Please select from the following options.\n1. Teller Options\n2. Customer Options\n3. Save Data\n4. Load Data\n5. Quit\n'))
            if choice == 5:
                print('Have a great day!')
                break
            
            elif choice == 1:
                while True:
                    t_choice = int(input('Welcome to the teller options. Please select from the following choice.\n1. Add Customer\n2. Add account\n3. Remove Account\n4. Quit\n'))
                    if t_choice == 4:
                        print('Have a great day!')
                        break
                    elif t_choice == 1: #create customer

                        id = input("Please enter ID.\n")
                        first_name = input("Please enter first name.\n")
                        last_name = input("Please enter last name.\n")
                        individual = Person(id, first_name, last_name)
                        self.bank.add_customer(individual)
                        print('self.customers: ' + str(self.bank.customers))

                    elif t_choice == 2:
                        account_num = int(input("Please enter an account number.\n"))
                        account_type = input("Please enter an account type.\n")
                        customer_id = int(input("Please enter customer ID.\n4"))
                        bank_account = Account(account_num, account_type, customer_id)
                        self.bank.add_account(bank_account)
                        print(self.bank.accounts)
                    
                    elif t_choice == 3:
                        print(self.bank.accounts)
                        account_to_delete = int(input("Please enter the account number you would like to delete.\n"))
                        self.bank.remove_account(account_to_delete)
            
            elif choice == 2:
                while True:
                    c_choice = int(input("Welcome to the customer options. Please select from the following choices.\n1. Balance Inquiry\n2. Deposit\n3. Withdrawl\n4. Quit\n"))
                    if c_choice == 4:
                        break
                    elif c_choice == 1:
                        account_number = int(input("Please enter the account number you would like to see the balance of.\n"))
                        print('accout num: ' + str(account_number))
                        value = self.bank.balance_inquiry(account_number)
                        print(value)
                    elif c_choice == 2:
                        account_num = int(input("Please enter the account you would like to deposit into.\n"))
                        amount = int(input("Please enter the amount you would like to deposit.\n"))
                        self.bank.deposit(account_num, amount)
                    elif c_choice == 3:
                        account_num = int(input("Please enter the account you would like to withdraw from.\n"))
                        amount = int(input("Please enter the amount you would like to withdraw.\n"))
                        self.bank.withdrawal(account_num, amount)

            elif choice == 3:
                self.bank.save_data()
            
            elif choice == 4:
                self.bank.load_data()














                


menu = Menu() # menu class needs an isntance of a bank class to perform functions on 
menu.interactive_term()

menu2 = Menu() # second interactive menu/bank