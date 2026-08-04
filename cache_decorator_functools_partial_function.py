
# @cache
# #jate same jinish ke bar bar calculation na kore store kore rake next time use korar jonno
# #something liek dp memoization 

# #Without cache decorator
import time

def fib(n):
    if n<=1:
        return 1
    return fib(n-1)+fib(n-2)
for i in range(37):
    print(i,fib(i))

end=time.time()
mili_seconds=(end-start)*1000
print('Time took: ',mili_seconds)

#Time took:  32269.845724105835


# #Without cache decorator
import time 
import functools

@functools.lru_cache(maxsize=128)
def fib(n):
    if n<=1:
        return 1
    return fib(n-1)+fib(n-2)

start=time.time()
for i in range(37):
    print(i,fib(i))

end=time.time()
mili_seconds=(end-start)*1000
print('Time took: ',mili_seconds)
#Time took:  5.000114440917969



#PARTIAL FUNCTION 
from functools import partial
def get_number(a,b,c,d):
    return a*1000+b*100+c*10+d

number=get_number(4,5,3,2)
aonly=partial(get_number,b=0,c=0,d=0)
num=aonly(4)
print(num)




