#%% Problem 1 

def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

#%% Problem 2 

class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
r = Rectangle(5, 10)
print(r.area())
print(r.perimeter())

#%% Problem 3

def count_words(string):
    string_dict = {} 
    for i in string.split(): # for i in k
        if i in string_dict.keys():
            string_dict[i] += 1 
        else: 
            string_dict[i] = 1
    return string_dict

string = "Hello world hello python"
print(count_words(string))

# %%
