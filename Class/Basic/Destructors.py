#To know more:https://www.geeksforgeeks.org/destructors-in-python/
'''
The __del__() method is a known as a destructor method in Python. 
It is called when all references to the object have been deleted i.e when an object is garbage collected. 

Syntax of destructor declaration : 
 
def __del__(self):
  # body of destructor

Example 1 : Here is the simple example of destructor. By using del keyword we deleted the all references of object ‘obj’, therefore destructor invoked automatically.
'''
#ex:1
class Employee:
      def __init__(self):
         print('Employee created')
      def __del__(self):
         print('Destructor called, Employee deleted.')

obj= Employee()
del obj

'''
Note : The destructor was called after the program ended or when all the 
references to object are deleted i.e when the reference count becomes zero, 
not when object went out of scope
'''


#EX:2

# Python program to illustrate destructor
#This example gives the explanation of above-mentioned note. 
class Employee:

	# Initializing
	def __init__(self):
		print('Employee created')#3

	# Calling destructor
	def __del__(self):
		print("Destructor called")#6

def Create_obj():
	print('Making Object...')#2
	obj = Employee()
	print('function end...')#4
	return obj

print('Calling Create_obj() function...')#1
obj = Create_obj()
print('Program End...')#5

'''
Output

Calling Create_obj() function...
Making Object...
Employee created
function end...
Program End...
Destructor called

Here, notice that the destructor is called after the ‘Program End…’ printed.
'''






