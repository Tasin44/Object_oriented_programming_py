'''
The word polymorphism means having many forms. 
In programming,polymorphism means the same function name (but different signatures) 
being used for different types. 
or 
Polymorphism means same method name behaves differently depending on the object.

The key difference is the data types and number of arguments used in function.
'''
#Example-1: inbuilt polymorphic functions:

# len() being used for a string
print(len("geeks"))#len 5

# len() being used for a list
print(len([10, 20, 30]))#len 3


#Examples 2: user-defined polymorphic functions: 

def add(x, y, z = 0): 
    return x + y+z

# Driver code 
print(add(7, 3))
print(add(2, 3, 11))

'''
Real life example :
Real-Life Example: Payment Methods
Imagine you are at a store and you want to pay for your items. There are multiple ways to pay: cash, credit card, mobile payment (like Apple Pay or Google Pay), or even a check.

    Cash Payment: When you pay with cash, the cashier takes the money, counts it, and gives you change if necessary.
    Credit Card Payment: When you pay with a credit card, the cashier swipes the card through a machine, which processes the payment and prints a receipt.
    Mobile Payment: When you pay with a mobile payment app, you hold your phone near the payment terminal, and the transaction is processed wirelessly.
    Check Payment: When you pay with a check, you write the amount, sign the check, and give it to the cashier, who then processes it through the bank.

In this scenario, the act of "paying" is polymorphic. The cashier's action (the function) changes based on the type of payment method (the object) you choose. 
This is similar to how polymorphism works in programming, where a single function can handle different types of objects in different ways.
'''


