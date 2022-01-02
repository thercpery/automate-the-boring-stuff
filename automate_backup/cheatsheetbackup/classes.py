# A class is like a blueprint for creating objects. An object has properties and methods (functions) associated with it. Almost anything in Python is an object

# Create a class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    
    def greeting(self):
        return f'My name is {self.name}, and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# Extend class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name}, and I am {self.age}, and my balance is {self.balance}'


# Initialize user object
rc = User('RC Pery', 'rcpery@something.com', 24)

# print(type(rc))
# print(rc.name)
# print(rc.age)
# print(rc.email)

# Initialize customer object
jane = Customer('Jane Smith', 'jane@yahoo.com', 34)
jane.set_balance(500)
print(jane.greeting())


rc.has_birthday()
print(rc.greeting())