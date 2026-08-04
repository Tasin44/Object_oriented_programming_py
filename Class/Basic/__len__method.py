'''
The __len__ method is used to define how the length of an object of a 
custom class is determined. When you call the built-in len() function on an object, 
Python internally looks for the presence of the __len__ method within that object's class. 
If the __len__ method is defined, Python invokes it to determine the length of the object.

The len() function is commonly used with built-in data 
types like lists, tuples, strings, dictionaries, etc to find their length.
'''
my_list = [1, 2, 3, 4]
print(len(my_list))  # Output: 4

my_tuple = (1, 2, 3)
print(len(my_tuple))  # Output: 3

my_string = "Hello, World!"
print(len(my_string))  # Output: 13

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(len(my_dict))  # Output: 3

my_set = {1, 2, 3, 4, 5}
print(len(my_set))  # Output: 5

my_range = range(1, 10)  # From 1 to 9 (inclusive)
print(len(my_range))  # Output: 9

'''
Custom Objects

You can also define custom objects that support 
the len() function by implementing the __len__ method.
In this below custom class, the __len__ method is defined to 
return the length of the internal list items.

'''
class MyList:
    def __init__(self, data):
        self.data = data
        # print(data) 
    def __len__(self):
        return len(self.data)

# Create an instance of MyList
my_list = MyList([1, 2, 3, 4, 5])

# Call len() on the object
print(len(my_list))  # Output: 5





