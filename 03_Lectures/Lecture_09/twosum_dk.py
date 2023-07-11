#%%
import numpy as np
import time 

nums = np.random.randint(1, 100, 100)
target = np.random.randint(1, max(nums)*2)
print(f"target is: {target}")
#%%
start = time.time()

found = False
while found == False: 
    ind_1 = np.random.randint(0, 100)
    ind_2 = np.random.randint(0, 100)
    if ind_1 == ind_2: 
        pass 
    else: 
        if ind_1 + ind_2 == target: 
            found = True
            print(f"index 1: {ind_1}")
            print(f"index 2: {ind_2}")

end = time.time()
print((end-start)*100)
#%%