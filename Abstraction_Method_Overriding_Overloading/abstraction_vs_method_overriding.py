

#Does abstraction and method overriding same thing?

'''
বিষয়টা ঠিক এভাবেই কাজ করে:

    -অ্যাবস্ট্রাকশন (Abstraction):প্যারেন্ট ক্লাসে মেথড শুধু ডিক্লেয়ার বা ডিফাইন করা থাকে (ভেতরে কোনো কোড থাকে না, শুধু pass থাকে)। 
    চাইল্ড ক্লাসকে বাধ্য হয়ে সেই মেথডটির ভেতরে কোড লিখে ইমপ্লিমেন্ট করতে হয়।

    -মেথড ওভাররাইডিং (Method Overriding): প্যারেন্ট ক্লাসে আগে থেকে কাজ করছে এমন কোনো মেথডকে চাইল্ড ক্লাসে নিজের প্রয়োজন মতো পরিবর্তন (modify) 
    করে বা নতুন করে লেখাই হলো ওভাররাইডিং।

ছোট্ট একটি টেকনিক্যাল পয়েন্ট:
অ্যাবস্ট্রাকশনের ক্ষেত্রে চাইল্ড ক্লাস যখন প্যারেন্টের ওই ফাঁকা (abstract) মেথডটাকে ইমপ্লিমেন্ট করে, 
প্রোগ্রামিংয়ের ভাষায় সেই কাজটাকেও 'মেথড ওভাররাইডিং'-ই বলা হয়। 
অর্থাৎ, প্যারেন্টের মেথড ফাঁকা থাকুক বা আগে থেকেই ইমপ্লিমেন্ট করা থাকুক—চাইল্ড ক্লাসে এসে সেই একই নামের মেথড পুনরায় লেখা হলেই সেটাকে ওভাররাইডিং বলে।


সহজ কথায়:
    -অ্যাবস্ট্রাকশন হলো নিয়ম (প্যারেন্ট বলে দেয়: "এই মেথডটা থাকতেই হবে")।
    -ওভাররাইডিং হলো কাজ (চাইল্ড বলে: "আমি প্যারেন্টের মেথডটাকে নিজের মতো করে লিখলাম")।
'''
'''
Think of it this way

Suppose you say:

"Every payment method must have a pay() method."

That's abstraction.

You don't care how each payment method pays. You only define the requirement:
'''

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Now different classes implement it:

class Bkash(Payment):
    def pay(self, amount):
        print("Paying with bKash")


class Stripe(Payment):
    def pay(self, amount):
        print("Paying with Stripe")

'''
Here, Payment says:

"You must have pay()."

That's abstraction.

So where is overriding?

Suppose you have:
'''


class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def sound(self):
        print("Bark")

'''
Dog already inherits sound() from Animal, but provides a different implementation.

That's method overriding.
'''

# Parent: sound() → "Some sound"
# Child: sound() → "Bark"

'''
|                           | Abstraction                             | Method Overriding                     |
| ------------------------- | --------------------------------------- | ------------------------------------- |
| Main purpose              | Hide implementation / define a contract | Change inherited behavior             |
| Requires inheritance?     | Usually yes                             | **Yes**                               |
| Parent method must exist? | Abstract method exists as a requirement | **Yes**, inherited method exists      |
| Child implementation?     | Usually required                        | Optional, but done to change behavior |




'''

'''
Both can involve a parent → child relationship and the child can provide its own implementation.
That's why they seem similar.
But remember this simple rule:

Abstraction = "You must implement this."
Overriding = "I'm changing how this inherited method works."

And importantly, an abstract method can also be overridden. That's where the two concepts can appear together.
'''










