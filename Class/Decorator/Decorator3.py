#                                                '''
                                                #Question:find out the execution time of a function using a decorator.
#                                                '''
# importing libraries
import time
import math

# decorator to calculate duration taken by any function.
#Decorator Definition:
def calculate_time(factoria):
    '''
    This function holds the timing logic,
    we can apply this logic to any function with the help of Decorator
    '''
    def inner1(*args, **kwargs):

        # storing time before function execution
        begin = time.time()
        
        factoria(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", factoria.__name__, end - begin)

    return inner1

#Decorator Application:
@calculate_time
def factorial(num):

# sleep 2 seconds because it takes very less time so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))

# calling the function.
factorial(10)

'''
✅ Step-by-step Execution
1. Decorator Definition

def calculate_time(factoria):

    Step 1: A function named calculate_time is defined, which accepts another function (factoria) as an argument.

    Purpose: This is the decorator function that wraps another function with timing logic.

    def inner1(*args, **kwargs):

    Step 2: Inside calculate_time, another function inner1 is defined. This will replace the original factorial function.

    Purpose: inner1 will add extra functionality — in this case, timing.

        begin = time.time()

    Step 3: Start timer right before calling the actual function.

        factoria(*args, **kwargs)

    Step 4: Call the original function (factorial) passed to the decorator with any arguments.

    Note: This is where the original logic (sleep + factorial calculation) happens.

        end = time.time()

    Step 5: End timer after function execution finishes.

        print("Total time taken in : ", factoria.__name__, end - begin)

    Step 6: Print the time taken for the function to run.

    return inner1

    Step 7: Return the inner1 function, which now includes timing logic.

    Effect: factorial = calculate_time(factorial) implicitly because of the decorator syntax.

🧠 Behind the Scenes: Decorator Application

@calculate_time
def factorial(num):

    Step 8: The @calculate_time decorator is applied to the factorial function.

    Effect: Python translates this as:

factorial = calculate_time(factorial)

Now factorial refers to inner1, not the original function.
🔁 Function Call

factorial(10)

    Step 9: You're calling inner1(10) now.

    Inside inner1:

        Time starts

        time.sleep(2) and math.factorial(10) run

        Time ends

        Duration is printed

🧾 Final Output Example:

3628800
Total time taken in :  factorial 2.002134084701538
'''

#===============================================================================================================================================
'''

If we want to do it without decorator:
'''

# importing libraries
import time
import math

# decorator to calculate duration taken by any function.
#Decorator Definition:
def calculate_time(factorialf):
  
    '''
    This function holds the timing logic,
    we can apply this logic to any function with the help of Decorator
    '''
    
    def inner1(*args, **kwargs):

        # storing time before function execution
        begin = time.time()
        
        factorialf(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", factorialf.__name__, end - begin)

    return inner1

#Without Decorator Application:
'''
@calculate_time
def factorial(num):

# sleep 2 seconds because factorial calculation takes very less time so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))

# calling the function.
factorial(10)
'''

def factorial(num):

    begin = time.time()  # Manually measure time (timing start)
    
    time.sleep(2)
    result = math.factorial(num)
    print(result)
     
    end = time.time()   # Manually measure time (timing end )
    print("Total time taken in: factorial", end - begin)
print("Total time taken in : factorial", end - start)



