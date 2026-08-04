class Calculator:
    def add(self,x,y):
        return x+y
    def mult(self,x,y):
        return x*y
    def div(self,x,y):
        return x/y
    def sub(self,x,y):
        return x-y

c1=Calculator()
print(c1.add(5,7))
print(c1.mult(5,7))
print(c1.div(28,7))
print(c1.sub(21,7))