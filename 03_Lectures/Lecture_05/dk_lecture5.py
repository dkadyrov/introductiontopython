#%%
var = "columbia"
year = 2023

print("I am at " + var + " for summer " + str(year))
print(f"I am at {var} for summer {year}")
print("I am at {} for summer {}".format(var, year))
# %%

class Person(object): 
    def __init__(self, username, password): 
        self.username = username
        self.password = password
        self.photo = None
        self.email = None
        self.phone = None

    def parse_email(self, string):
        # checks what email is an email      
        if "@" in string: 
            return True
        else: 
            return False

    def capitalize_name(self):
        return self.username.capitalize()

person = Person(username="daniel", password="password")
# %%

class Animal(object):
    def __init__(self):
        self.name = None
        self.fur = None
        self.legs = None 
        self.type = None
        self.sleep = False
        self.food_amount = 0 

    def sleeping(self): 
        self.sleep = True

    def hungry(self):
        self.food_amount = 0 

    def eaten(self):
        self.food_amount = 100

class Dog(Animal): 
    def __init__(self, name): 
        Animal.__init__(self) 
        self.legs = 4
        
a = Animal()
d = Dog(name="Karl Marx")
# %%
import numpy as np 

class Circle(object):
    def __init__(self, radius): 
        self.radius = radius
        self.area = self.calculate_area(self.radius)
        self.circumference = self.calculate_circumference(self.radius)
    
    def calculate_area(self, radius): 
        return np.pi * radius ** 2
    
    def calculate_circumference(self, radius): 
        return 2*np.pi * radius
    
circle = Circle(radius=2)
circle.calculate_area(radius=3)


circle2 = Circle(radius=3)
print(circle2.area)
# %%
string = "test"

string.capitalize()
string.lower()
# %%
