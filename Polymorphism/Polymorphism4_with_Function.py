'''
Polymorphism with a Function and objects: 

It is also possible to create a function that can take any object, 
allowing for polymorphism. In this example, let’s create a function called “func()” 
which will take an object which we will name “obj”. 
Though we are using the name ‘obj’, any instantiated object will be able
to be called into this function. 
'''

class India():
    def capital(self):
        print("New Delhi is the capital of India.")
 
    def language(self):
        print("Hindi is the most widely spoken language of India.")
 
    def type(self):
        print("India is a developing country.")
 
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
 
    def language(self):
        print("English is the primary language of USA.")
 
    def type(self):
        print("USA is a developed country.")

def func(obj):
    obj.capital()
    obj.language()
    obj.type()
 
obj_ind = India()
obj_usa = USA()
 
func(obj_ind)
func(obj_usa)

'''
Output

New Delhi is the capital of India.
Hindi is the most widely spoken language of India.
India is a developing country.
Washington, D.C. is the capital of USA.
English is the primary language of USA.
USA is a developed country.
'''