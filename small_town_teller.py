import pickle

class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
    
    def __repr__(self):
        return self.first_name + ' ' + self.last_name

class Account:
    def __init__(self, number, type, owner):
        self.number = number
        self.type = type
        self.owner = owner
        self.balance = 0
    
    def __repr__(self):
        return self.number 

class Bank:
    def __init__(self):
        self.customers = {1: ['Sean', 'Lan']}
        self.accounts = {100: ['1', 'Checking', 1, 1000]}

    def add_customer(self, customer):
        if customer.id not in self.customers:
            self.customers[customer.id] = [customer.first_name, customer.last_name]
            print('Customer ' + str(customer.id) + ' added. List of current customers: ' + str(self.customers) + '\n')
            return
        else:
            print('Customer id ' + str(customer.id) + ' already exists in Bank!\n')
            return

    def add_account(self, account):
        #print('keys: ' + str(self.accounts.keys()) + 'owner id: ' + str(account.owner))
        try:
            if account.number not in self.accounts.keys() and account.owner in self.customers.keys():
                self.accounts[account.number] = [account.type, account.owner, account.balance]
                print('Account ' + str(account.number) + ' added. List of current accounts ' + str(self.accounts) + '\n')
                return
        except AttributeError:
            print('Account id ' + str(account.owner) + ' already exists in accounts or customer does not exist in bank.\n')
            return
   
    def remove_account(self, account_num):
        #print(self.accounts, str(account.number))
        try:
            del self.accounts[account_num]
            print('Account ' + str(account_num) + ' removed. List of current accounts: ' + str(self.accounts) + '\n')
        except NameError:
            print('This account cannot be removed because it does not exist.\n')
    
    def balance_inquiry(self, accountNum):
        print(accountNum)
        if accountNum not in self.accounts.keys():
            print('Your account number does not exist')
        else:
            return 'Balance Inquiry: Account number ' + str(accountNum) + ' has a balance of ' + '{:.2f}'.format(self.accounts[accountNum][3]) + ' dollars\n'


    def deposit(self, account, money):
        if account in self.accounts.keys():

            self.accounts[account][3] += money
            print('Deposit: ' + '{:.2f}'.format(money) + ' was deposited into Account ' + str(account) + ' and the current balance is ' + '{:.2f}'.format(self.accounts[account][3]) + '\n')
        else:

            print('Your account does not exist')
        return 


    def withdrawal(self, account, money):
        if account not in self.accounts.keys():
            print('Your account does not exist')
        else:
            self.accounts[account][3] -= money
            print('Withdrawal: ' + '{:.2f}'.format(money) + ' was withdrawn from Account ' + str(account) + ' and the current balance is ' +  '{:.2f}'.format(self.accounts[account][3]) + '\n')
            return

    def save_data(self):
        currentInfo = [self.customers, self.accounts]
        with open('/Users/sean/labs/PyPart10/cust_accounts saved', 'wb') as f:
            pickle.dump(currentInfo, f)

    def load_data(self):
        with open('/Users/sean/labs/PyPart10/cust_accounts saved', 'rb') as f:
            loaded = pickle.load(f)
        del(self.customers)
        del(self.accounts)
        self.customers = loaded[0]
        self.accounts = loaded[1]
        #print(type(loaded))
        print(self.customers)
        print(self.accounts)
        #return loaded
    
