#%%
import pandas as pd 

data = pd.read_csv("cereal.csv")
#%%
# Problem 2 
data.head(5)

#%% Problem 3
data.describe()

#%% Problem 4
data.corr()

#%% Problem 5

pd.plotter.scatter_matrix(data, alpha=0.2)

#%% Problem 6
snip = data[["name", "mfr", "rating"]]

mfr = data["mfr"].value_counts()
x = mfr.index
y = mfr.values

import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x=data["mfr"].value_counts().index,
        y=data["mfr"].value_counts().values
    )
)
fig.update_layout(
    xaxis_title="Manufacturer",
    yaxis_title="Count"
)
fig.show()
# value_counts 
# %%
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=data["sugars"],
        y=data["rating"],
        mode="markers"
    )
)
fig.update_layout(
    xaxis_title="Sugars",
    yaxis_title="Rating"
)
fig.show()
#%%
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=data["calories"],
        y=data["weight"],
        mode="markers"
    )
)
fig.update_layout(
    xaxis_title="Calories",
    yaxis_title="Weight"
)
fig.show()
#%%%
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=data["shelf"],
        y=data["rating"],
        mode="markers"
    )
)
fig.update_layout(
    xaxis_title="Shelf",
    yaxis_title="Rating"
)
fig.show()

#%%



#%%
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
