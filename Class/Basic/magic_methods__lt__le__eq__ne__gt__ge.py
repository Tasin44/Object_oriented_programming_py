#See details in docs
'''
Why _lt, ___le__ this type of magic method is need? Can't i use if else inside the cls to do the same work?
    Enables comparison operations (<, <=) between objects.
    Without them, if obj1 < obj2 would raise TypeError.
    
'''


#These are magic methods that define comparison behavior.

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    # They are all boolean method
    def __lt__(self,other):
        return(self.x,self.y)<(other.x,other.y)
    def __le__(self,other):
        return(self.x,self.y)<=(other.x,other.y)
    def __eq__(self,other):
        return(self.x,self.y)==(other.x,other.y)
    def __ne__(self,other):
        return(self.x,self.y)!=(other.x,other.y)
    def __gt__(self,other):
        return(self.x,self.y)>(other.x,other.y) 
    def __ge__(self,other):
        return(self.x,self.y)>=(other.x,other.y)

point1=Point(5,2)
point2=Point(3,4)


print("point1 < point2:", point1 < point2)
print("point1 <= point2:", point1 <= point2)
print("point1 == point2:", point1 == point2)
print("point1 != point2:", point1 != point2)
print("point1 > point2:", point1 > point2)
print("point1 >= point2:", point1 >= point2)

'''
in lexicographical order, (5, 2) is greater than (3, 4) because 5 > 3.
Therefore, point1 > point2 evaluates to True.
'''

#if we want to compare by user defined function
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def greater(self,other):
        return (self.x,self.y)>(other.x,other.y)

point1=Point(5,2)
point2=Point(8,9)
point3=Point(1,3)

print("point2 > point1", point1.greater(point2))

print("point2 > point1 and point1>point3 and point2<point3:", point1.greater(point2),point1.greater(point3),point3.greater(point2))
        
print("point2 > point1 and point1>point3 and point2<point3:", point2.greater(point1),point2.greater(point3),point2.greater(point1))


'''
✅ Why not use if-else/Why Magic Methods uses instead of if/else??

    No, because Python expects special methods for operators.

    "if obj1 < obj2" automatically calls obj1.__lt__(obj2).

    Without __lt__, Python wouldn’t know how to compare them.

'''
#Example:

class Box:
    def __init__(self, weight):
        self.weight = weight

    def __lt__(self, other):  # define < between boxes
        return self.weight < other.weight

box1 = Box(10)
box2 = Box(20)

print(box1 < box2)  # True, because 10 < 20

'''
Without __lt__, Python will throw an error:
TypeError: '<' not supported between instances of 'Box' and 'Box'
'''
#like if we do(another example):

class Person:
    def __init__(self, age):
        self.age = age

p1 = Person(25)
p2 = Person(30)

if p1 < p2:  # TypeError: '<' not supported
    print("p1 is younger")
'''
TypeError: '<' not supported between instances of 'Person' and 'Person'
'''








