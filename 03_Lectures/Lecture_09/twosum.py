#%%
import numpy as np
import time 

# nums = np.random.randint(1, 100, 100)
# target = np.random.randint(1, max(nums)*2)
nums = np.array([53, 79, 21, 21, 98, 16, 49, 92, 42, 75, 89, 43, 88, 43, 97, 47, 66,
       42, 68, 97, 26, 39, 67, 87, 81, 84, 35,  4, 99, 17, 60, 47, 47, 78,
       59, 25, 80, 55, 65, 71, 36, 79,  2, 80, 20, 94, 29,  7, 40, 39, 97,
       25, 70, 60, 50, 58, 13, 31, 68, 87, 80, 28, 44,  7, 12, 63, 11, 47,
        9, 31, 80, 95, 87,  2, 74, 39,  6, 89, 27, 58, 93, 56, 75, 47, 49,
        6, 72, 19, 61,  5, 89, 80, 56, 77, 13, 40, 72, 23, 37, 41])

target = 186

print(f"target is: {target}")
#%%
start = time.time()

found = False
while found == False: 
    ind_1 = np.random.randint(0, 100)
    ind_2 = np.random.randint(0, 100)
    if nums[ind_1] == nums[ind_2]: 
        pass 
    else: 
        if nums[ind_1] + nums[ind_2] == target: 
            found = True
            print(f"index 1: Number {nums[ind_1]} at {ind_1}")
            print(f"index 2: Number {nums[ind_2]} at {ind_2}")

end = time.time()
print((end-start)*100)
#%%