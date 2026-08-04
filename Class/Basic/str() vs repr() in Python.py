'''
In Python, the str() and repr() functions are used to obtain string representations of objects.
'''


s = 'Hello, Geeks.'
print (str(s))
print (str(2.0/11.0))

# Output:
# Hello, Geeks.
# 0.181818181818

Python repr()


s = 'Hello, Geeks.'
print (repr(s))
print (repr(2.0/11.0))

Output:

'Hello, Geeks.'
0.18181818181818182

'''
From the above output, we can see if we print a string using the repr() function then it prints with a pair of quotes 
and if we calculate a value we get a more precise value than the str() function.
'''
Difference between Python str() and Python repr()

Return Value
Returns a human-readable string representation of the object
Returns an unambiguous(Technical/debugging description) string representation of the object
like Example Output	for str "John, 36 years old"	, repr "Person(name='John', age=36)"
Usage
Used for creating user-friendly output and for displaying the object as a string
Used for debugging and development purposes to get the complete information of an object

Examples
str(123) returns ‘123’
repr(123) returns ‘123’

str(‘hello’) returns ‘hello’
repr(‘hello’) returns “‘hello'”

str([1, 2, 3]) returns ‘[1, 2, 3]’
repr([1, 2, 3]) returns ‘[1, 2, 3]’

str({‘name’: ‘John’, ‘age’: 30}) returns “{‘name’: ‘John’, ‘age’: 30}”
repr({‘name’: ‘John’, ‘age’: 30}) returns “{‘name’: ‘John’, ‘age’: 30}”



