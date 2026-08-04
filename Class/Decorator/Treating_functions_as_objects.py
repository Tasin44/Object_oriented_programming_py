
# Define a function named shout that takes a string parameter text
def shout(text):
    return text.upper()# Return the uppercase version of the input text

print(shout('HeLlo'))# Call the shout function with 'Hello' as the argument and print the result

new_assigning=shout# Assign the shout function to a new variable named new_assigning

print(new_assigning('TaSin'))
print(new_assigning('RahIm'))
print(new_assigning('JaMall'))

'''
output:
HELLO
TASIN
RAHIM
JAMAL 
'''

# Call the new variable (which now holds the shout function) 
# with 'Hello' as the argument and print the result
# It performs the same operation as shout('Hello'), resulting in 'HELLO' being printed again.

'''
In Python, functions are first-class citizens, 
meaning they can be assigned to variables and passed as arguments.And they can also
Returned from other functions.
'''
