
#Single inheritance example-3

'''
The super() function is a built-in function that returns the objects 
that represent the parent class. 
It allows to access the parent class’s methods and attributes in the child class.
It enabling you to extend and customize the functionality inherited from the parent class.

Multiple Inheritance: In cases of multiple inheritance,super() ensures that the method 
resolution order (MRO) is followed,and all necessary initializations are performed.

The super function should be called as a function like super()., not as a class attribute like super.
'''


'''
In django 
Why super().save(*args, **kwargs)?

It calls the parent class's save method to actually save the object to the database after your custom logic.
What are *args and **kwargs?

They capture and pass through any arguments the save method receives:

    *args = positional arguments (like force_insert, using)

    **kwargs = keyword arguments (like force_insert=True, using='default')

Example:
# When Django calls save with arguments:
article.save(force_insert=True, using='default')

# Without *args, **kwargs:
def save(self):
    super().save()  # ❌ Loses force_insert and using arguments

# With *args, **kwargs:
def save(self, *args, **kwargs):
    super().save(*args, **kwargs)  # ✅ Preserves all original arguments
'''


class Person(object):
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        return f"{self.name}\nhis id {self.id}\nincome: {self.salary}\ndesignation: {self.position}"
        #we can return f using both ' or "

class Employee(Person):
    def __init__(self,name,id,salary,position):

        # Initialize the parent class attributes first
        super().__init__(name,id)
        '''
        If don't invoke the __init__() of the parent class then 
        its instance variables would not be available to the child class.
        '''
        # Then initialize the child class specific attributes
        self.salary=salary
        self.position=position

obj=Employee("Tasin",62,62000,"intern")

print(obj.display())

'''
Order of Initialization:
1.The parent class attributes (name and id) are initialized first.
2.The child class specific attributes (salary and position) are initialized afterward.
'''
#=====================================================================================================================================================
#=====================================================================================================================================================
'''
Task: Build an Inventory class that stores items (dict of name → {price, qty}). Support adding items via **kwargs, a callable interface to quickly look up total value, 
and a DiscountInventory subclass that applies a discount using super().
'''

class Inventory:
    def __init__(self, **initial_items):
        # initial_items: name=(price, qty) pairs passed as kwargs
        self.items = {}
#       '''
#       The first line initializes an empty dictionary. The loop then populates it with any items passed during object creation. This allows you to create an inventory with initial items like:
#       '''
       
        for name, (price, qty) in initial_items.items():
            self.items[name] = {"price": price, "qty": qty}

    def add_items(self, *args):
        # args: tuples of (name, price, qty)
        for name, price, qty in args:
            if name in self.items:
                self.items[name]["qty"] += qty
            else:
                self.items[name] = {"price": price, "qty": qty}

    def remove_item(self, name):
        try:
            del self.items[name]
        except KeyError:
            print(f"Item '{name}' not found.")

    def total_value(self):
        return sum(v["price"] * v["qty"] for v in self.items.values())

    def __call__(self):
        # calling the object directly gives a quick summary
        return {name: v["qty"] for name, v in self.items.items()}


class DiscountInventory(Inventory):
    def __init__(self, discount_pct, **initial_items):
        super().__init__(**initial_items)
        self.discount_pct = discount_pct

    def total_value(self):
        original_total = super().total_value()
        return original_total * (1 - self.discount_pct / 100)


inv = DiscountInventory(discount_pct=10, apple=(2.0, 10), banana=(1.0, 20))
inv.add_items(("cherry", 5.0, 4), ("apple", 2.0, 5))  # adds cherry, adds qty to apple
inv.remove_item("kiwi")  # triggers except branch
print(inv.total_value())     # discounted total
print(inv())                 # uses __call__ -> {'apple': 15, 'banana': 20, 'cherry': 4}



'''
Here, at first I'm calling discount() class, in the discount class it's using parent class inventory init method, at first it initialize the product as initial items, then discount_pct, right?

So yes, the order is exactly:

Discount.__init__()
        │
        ▼
Inventory.__init__()
        │
        ▼
Create self.items
Store apple
Store banana
        │
        ▼
Return to Discount.__init__()
        │
        ▼
self.discount_pct = 10
'''

