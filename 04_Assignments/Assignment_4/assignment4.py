#%%
import pandas as pd 

data = pd.read_csv("cereal.csv")
# %%
# Option 1 
mfrs = data.mfr.unique()
factorize = {}
num = 0 
for i in mfrs: 
    factorize[i] = num
    num += 1   

data["mfr_num"] = data["mfr"].apply(lambda x: factorize[x])
data[["mfr", "mfr_num"]]
# %%
# Option 2 
codes, uniques = pd.factorize(data["mfr"])
data["mfr_num"] = codes
data[["mfr", "mfr_num"]]
# %%
import matplotlib.pyplot as plt


plt.bar(data["protein"], data["fat"])

# fig, ax = plt.subplots()
# ax.bar(data["protein"], data["fat"])
# %%
