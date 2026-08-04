
'''
.join() is a string method in Python that
concatenates the elements of an iterable 
(such as a list) into a single string, 
with the string it's called on used as 
a separator between each element.

The .join() method in Python works specifically
for iterable objects that contain strings,
such as lists, tuples, or sets where each element 
is a string. It doesn't directly work with 
dictionaries because dictionaries consist 
of key-value pairs,not just values.

'''       

# Using join with a list
my_list = ['apple', 'banana', 'orange']
result = " and ".join(my_list)
print(result)  # Output: apple and banana and orange

# Using join with a tuple
my_tuple = ('apple', 'banana', 'orange')
result = ", ".join(my_tuple)
print(result)  # Output: apple, banana, orange

# Using join with a set
my_set = {'apple', 'banana', 'orange'}
result = " & ".join(my_set)
print(result)  # Output: apple & orange & banana or banana & apple & orange
