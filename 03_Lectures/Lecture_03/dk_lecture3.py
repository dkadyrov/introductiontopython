#%%
def custom_print(my_string): 
    # This function prints my_string
    
    print(my_string)

custom_print("hello world")
custom_print(my_string="hello world")
#%%
custom_print("world hello")
# %%

def add_three_variables(x, y, z):
    # mathematical function 
    return x + y + z 

add_three_variables(1,2,3)
g = add_three_variables(5,6,7)
# %%
def list_maker(my_string, n=5):
    # function that returns a list of the string repeated a certain amount of times.

    lst = [my_string] * n

    return lst 

lst = list_maker("daniel", 2)
lst = list_maker("daniel")
# %%
def dict_changer(data, operation="capitalize"): 
    # Iterate through the values of a dictionary and perform a string operation on it. 

    #if type(data) != dict: 
    if not isinstance(data, dict):
        print("ERROR: Please input a dictionary for data")

    if operation == "capitalize": 
        for key in data.keys():
            data[key] = data[key].capitalize()
    elif operation == "lower":
        for key in data.keys():
            data[key] = data[key].lower()
    elif operation == "title": 
        for key in data.keys():
            data[key] = data[key].title()
    elif operation == "remove 2":
        for key in data.keys():
            data[key] = data[key][:-2]
    else: 
        print("ERROR. I don't support any other operation")

    return data

data = {
    "name": "daniel",
    "location": "New York City", 
    "drinking": "Coffee",
    "using": "Python"
}

ndata = dict_changer(data, operation="remove 3")
print(ndata)
# %%

string_multiplier = lambda string: string*5 + " " + string
string_multiplier("daniel")
# %%
import random

def my_own_random_function(): 
    return random.randint(0, 100)
# %%

def list_splitter(my_string, n=2): 
    # This function takes a string as an input and splits the string into a list at every word.  Print an error if the string is not instance of a string. At n string, capitaze the word. Accomodate for instances when the string is less than 2 words (hint, len() function). Return this list.
    
