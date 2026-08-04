
'''
Multiple inheritances: When a child class inherits from multiple parent classes, 
it is called multiple inheritances. 
In multiple inheritances, all the features of the base classes are inherited into the derived class. 
'''
=======================================================================================================================================================================
'''
# Example 1: (Without using super method) 
# If you don't want to use super() and **kwargs, you can explicitly call each parent's __init__:
# This works but is less flexible (breaks if inheritance hierarchy changes).
'''
class Father:
    def __init__(self, fname):
        self.fname = fname

class Mother:
    def __init__(self, mname):
        self.mname = mname
    
class Son(Father, Mother):
    def __init__(self, fname, mname):
        Father.__init__(self, fname)  # Explicitly call Father's init
        Mother.__init__(self, mname)  # Explicitly call Mother's init
    def display_parent_info(self):
        print("Father name: ", self.fname)
        print("Mother name: ", self.mname)

obj = Son("Nannu", "Taslima")
obj.display_parent_info()



================================================================================================================================================================================

Example 2: using super method

class Father:
    def __init__(self,fname):
        self.fname=fname

class Mother:
    def __init__(self,mname):
        self.mname=mname
    
class Son(Father,Mother):
    def __init__(self, fname,mname):
        super().__init__(fname) #We can also do :  Father.__init__(self, fname)
        #super().__init__(mname)  # ❌ Incorrect usage!
        Mother.__init__(self,mname)
    def display_parent_info(self):
        print("Father name: ", self.fname)
        print("Mother name: ",self.mname)

obj=Son("Nannu","Taslima")
obj.display_parent_info()



'''
Problem
#super().__init__(mname)  # ❌ Incorrect usage!

The main problem is with how you're using super() in multiple inheritance. 
When you call super().__init__() twice, it's not properly initializing both parent classes.

Because:
    super() does not support calling two parent constructors independently like that. 
    super() will follow the Method Resolution Order (MRO) and call the next class in line, not both separately.

❌If we try to do like:
    super().__init__(self, mname) is also incorrect usage — super().__init__() should not include self as an argument. 
    The correct form is just super().__init__(...) once for only one parent class. 

What's actually happening:

With class Son(Father, Mother), the MRO is:

Son -> Father -> Mother -> object

⭐So super().__init__(...) inside Son will call Father.__init__, and 
⭐super() in Father will call Mother.__init__ only if Father.__init__ used super() too.


But in your code:

    Father.__init__ does not use super(), so Mother.__init__ is never called.




Another explanation: 

We cann't use super() for all parent classes;
The super() mechanism works based on the Method Resolution Order (MRO), which means it only calls the next class 
in the inheritance chain as defined by the MRO.
Therefore, you cannot directly use super() to call both Father and Mother's __init__ methods
like super().__init__(fname)  
     super().__init__(mname)

According to the above code, the MRO is:

[Son, Father, Mother, object]

So, if you call super().__init__() in Son, it will invoke Father's __init__ method, but it won't automatically 
call Mother's __init__ method.
'''

=======================================================================================================================================================================

'''
But if we want to use super for both Father and Mother class:
There is a solution called 
Cooperative Multiple Inheritance
'''
#Cooperative Multiple Inheritance
class Father:
    def __init__(self, fname, **kwargs):
        super().__init__(**kwargs)
        self.fname = fname

class Mother:
    def __init__(self, mname, **kwargs):
        super().__init__(**kwargs)
        self.mname = mname
    
class Son(Father, Mother):
    def __init__(self, fname, mname):
        super().__init__(fname=fname, mname=mname)#This is using keyword arguments, not positional ones.
        #because of using **kwargs, if we change inheritance order (e.g., class Son(Mother, Father)), the argument order would break.
    def display_parent_info(self):
        print("Father name: ", self.fname)
        print("Mother name: ", self.mname)

obj = Son("Nannu", "Taslima")
obj.display_parent_info()

#To see the Method Resolution Order
print(Son.mro()) ## Output: [<class 'Son'>, <class 'Father'>, <class 'Mother'>, <class 'object'>]


'''
❓ why we use **kwargs in the __init__ methods of Father and Mother

✅ **kwargs is used when you're passing named keyword arguments like fname=fname, mname=mname.
✅ *args is used for positional arguments like (fname, mname).

The reason we use **kwargs in this case is to allow cooperative multiple inheritance, 
where each parent class's __init__ can safely accept and forward extra arguments to the next class in the 
Method Resolution Order (MRO).


How It Works (Step-by-Step)

    Method Resolution Order (MRO)

        When Son inherits from both Father and Mother, Python determines the order in which methods are called using MRO.

        You can check MRO using Son.__mro__ or Son.mro():
        

                print(Son.mro())  
                # Output: [<class 'Son'>, <class 'Father'>, <class 'Mother'>, <class 'object'>]

    This means:

        Son.__init__ → Father.__init__ → Mother.__init__ → object.__init__.
        


✔️✔️super().__init__() Calls in Chain

    ✔️When Son.__init__ calls super().__init__(fname=fname, mname=mname), it passes both fname and mname as keyword arguments.

    ✔️Father.__init__ takes fname and **kwargs:

        It sets self.fname = fname.

        Then calls super().__init__(**kwargs), forwarding remaining arguments (mname).

    ✔️Mother.__init__ receives mname (from **kwargs):

        It sets self.mname = mname.

        Then calls super().__init__() (which goes to object.__init__, doing nothing).

✔️✔️Why **kwargs is Necessary

    Without **kwargs, Father.__init__ would not be able to forward mname to Mother.__init__, causing an error.

    Example of what happens without **kwargs:
    
    
          class Father:
              def __init__(self, fname):  # Doesn't accept extra args
                  self.fname = fname
                  super().__init__()  # Error: Mother.__init__ misses mname

    This would fail because Mother.__init__ expects mname, but Father.__init__ doesn't pass it forward.


Alternative Approach (Explicit Calls)

    If you don't want to use super() and **kwargs, you can explicitly call each parent's __init__:
    

        class Son(Father, Mother):
            def __init__(self, fname, mname):
                Father.__init__(self, fname)  # Direct call
                Mother.__init__(self, mname)  # Direct call

This works but is less flexible (breaks if inheritance hierarchy changes).

'''
================================================================================================================================================

# using *args 

class Father:
    def __init__(self, fname, *args):
        self.fname = fname
        super().__init__(*args)

class Mother:
    def __init__(self, mname, *args):
        self.mname = mname
        super().__init__(*args)

class Son(Father, Mother):# if we change inheritance order (e.g., class Son(Mother, Father)), the argument order would break.
    def __init__(self, fname, mname):
        super().__init__(fname, mname)
    def display_parent_info(self):
        print("Father name: ", self.fname)
        print("Mother name: ", self.mname)


obj = Son("Nannu", "Taslima")
obj.display_parent_info()


'''
Why This Fails

    When Son.__init__ calls super().__init__(fname, mname), it passes them as positional args:

        Father.__init__(self, "Nannu", "Taslima")

        Father takes fname="Nannu" and forwards *args = ("Taslima",) to Mother.__init__.

        Mother.__init__(self, "Taslima") takes mname="Taslima" and forwards nothing to object.__init__.

    This works in this simple case, but it's fragile!

        ✅If we later change inheritance order (e.g., class Son(Mother, Father)), the argument order would break,it'll then give output like 
                Father name:  Taslima
                Mother name:  Nannu
                
          But if we use **kwargs ,even if we change the order like class Son(Mother,Father): the output not changed. 
          We've to call the class same way in both cases :
              obj = Son("Nannu", "Taslima")
       ✅ If a parent class adds a new required argument, all classes must adjust their *args handling.
'''
