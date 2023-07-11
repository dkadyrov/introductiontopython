#%%
import time 
import numpy as np 

#%%

x = np.random.randint(0, 100, 100000)
random_number = np.random.randint(0, 100)

#%%
def loop_forward(lst, num):
    start = time.time()
    for i in range(len(lst)): 
        if lst[i] == random_number:
            print(f"Found it at index {i}")
            break 
    end = time.time()

    return (end-start)*100

def loop_forward_cut(lst, num, cut=2):
    start = time.time()
    test = False
    for i in lst[:int(len(lst)/cut)]: 
        if i == num:
            print("Found it")
            test = True
            break 

    if test == False:
        for i in lst[int(len(lst)/cut):]: 
            if i == num:
                print("Found it")
                test = True
                break  
    end = time.time()  
    return (end-start)*100

def loop_forward_backward_cut(lst, num, cut=2):
    start = time.time()
    test = False
    for i in lst[:int(len(lst)/cut)]: 
        if i == num:
            print("Found it")
            test = True
            break 

    if test == False:
        lst = lst[int(len(lst)/cut):]
        for i in lst[::-1]: 
            if i == num:
                print("Found it")
                test = True
                break  
    end = time.time()  
    return (end-start)*100

#%%
print(f"I want to find {random_number}")
print(loop_forward(x, random_number))
print(loop_forward_cut(x, random_number, 2))
print(loop_forward_backward_cut(x, random_number, 2))
# %%
