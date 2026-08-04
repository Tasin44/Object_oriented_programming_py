class Bank:
    def __init__(self, name, password, balance, minlimit, maxlimit):
        self.name = name
        self.password = password
        self.balance = balance
        self.minlimit = minlimit
        self.maxlimit = maxlimit

    def get_balance(self):
        return self.balance 

    def deposit(self, name, password, amount):
        if self.authentication(name, password):
            self.balance += amount
            return f'After depositing {amount}, current balance is: {self.balance}'
        else:
            return f'Invalid credentials! Please try again.'

    def authentication(self, name, password):
        return name == self.name and password == self.password

    def withdraw(self, name, password, amount):
        if self.authentication(name, password):
            if self.minlimit <= amount <= self.maxlimit:
                self.balance -= amount
                return f'Withdrawal successful. Amount withdrawn: {amount} .Current balance: {self.balance}'
            else:
                return 'Please enter a valid amount between 500 to 5000'
        else:
            return f'Invalid credentials! Please try again.'



my_account = Bank("Tasin Mahmud", "tasin44", 20000, 500, 5000)
#my_account is an instance of the Bank class

# Authentication
name = input("Enter User Name: ")
password = input("Enter Password: ")
authenticated = my_account.authentication(name, password)

'''
This line calls the authentication method 
of the Bank class on the my_account instance, 
passing name and password as arguments.

Here:
.authentication(name, password): 

Calls the authentication method of the my_account
instance with name and password as arguments.

The method checks if the provided name 
and password match the instances name 
and password attributes and returns True 
if they do, otherwise False.
'''

while not authenticated:
    print("Invalid name or password. Please try again.")
    #jodi invalid input deya hoy,then try again asar por 
    #jeno punoray input chay tai name & password agian input chawa hoyeche
    name = input("Enter User Name: ")
    password = input("Enter Password: ")
    authenticated = my_account.authentication(name, password)

print("Authentication successful. Current balance:", my_account.get_balance())

# Transaction menu
while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    option = int(input("Enter your choice: "))

    if option == 1 :
        deposit_amount = input("Enter amount you want to deposit: ")
        try:
            deposit_amount = float(deposit_amount)
            print(my_account.deposit(name, password, deposit_amount))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif option == 2 :
        withdraw_amount = input("Enter amount you want to withdraw: ")
        try:
            withdraw_amount = float(withdraw_amount)
            print(my_account.withdraw(name, password, withdraw_amount))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif option == 3 :
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

'''
##Explanation of try and except:
try: 
This block contains code that might cause an exception. 
In your case,it attempts to convert deposit_amount to a float.

except:
This block executes if an exception occurs in the try block. 
Specifically,if a ValueError occurs 
(which happens if the input cannot be converted to a float), 
the except block will run, printing an error message.


##Can you use try and except only in if and elif?

No,you can use try and except anywhere in your code. 
They are not limited to if and elif statements. 
You can use them in any block of code where you 
expect an exception might occur and want to handle it gracefully.
'''