#%%
lst = [1,2,3,4,5]

for item in lst: 
    print(item) 

#%%
for item in lst:
    string = "My number is now: " + str(item)

    print(string) 
# %%
for item in lst:
    string = "My number is now: {}".format(item)

    print(string) 
# %%
for item in lst:
    string = f"My number is now: {item}"

    print(string) 
# %%
i = 0 
for item in lst: 
    z = item + i 
    i = i + 1 
    print(z)

# %%
person = {
    "name": "daniel",
    "age": 30,
    "height": 6, 
    "zoom": True
}

for a in person.keys():
    # print(a) 
    # print(person[a])
    print(f"The persons {a} is {person[a]}")

# %%
multiplier = 0 
for i in range(100):
    multiplier += i
# %%
for i in range(0, 100, 10): 
    print(i)
# %%
i = 0 
while i <= 5: 
    i += 1 
    print(i)
    
# %%
string = "The fox jumped over the lazy dog"
string = string.split()

i = 0 
s = string[i]
while s !=  "lazy":
    s = string[i]
    print(string[i])
    i += 1 

# %%
x = 10 

if x > 0: 
    print("x is positive")
elif x < 0:
    print("x is negative")
else: 
    print("x is zero")
# %%
