#Chaining Decorators
#In simpler terms chaining decorators means decorating a function with multiple decorators.
# code for testing decorator chaining 
def decor1(func): 
    def inner(): 
        x = func() 
        return x * x 
    return inner 

def decor(func): 
    def inner(): 
        x = func() 
        return 2 * x 
    return inner 

#Functions(num & num2 ) with Decorator Chaining:
@decor1
@decor
def num(): 
    return 10

'''
The num function first decorated with decor and then with decor1.
This is equivalent to num = decor1(decor(num)).
'''

@decor
@decor1
def num2():
    return 10
'''
The num2 function first decorated with decor1 and then with decor.
This is equivalent to num2 = decor(decor1(num2)).
'''


print(num()) 
print(num2())


'''
Output wiht explanation:

Decorating num:

num = decor(num):
    The num function returns 10.
    decor modifies this to 2 * 10 = 20.
num = decor1(decor(num)):
    The modified num now returns 20.
    decor1 modifies this to 20 * 20 = 400.


Decorating num2:

num2 = decor1(num2):
    The num2 function returns 10.
    decor1 modifies this to 10 * 10 = 100.
num2 = decor(decor1(num2)):
    The modified num2 now returns 100.
    decor modifies this to 2 * 100 = 200.
'''
