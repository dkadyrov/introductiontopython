#%% 
import numpy as np

data_x = np.linspace(0, 2*np.pi, 100)
data_y = np.sin(data_x)

#%%
# MATPLOTLIB
import matplotlib.pyplot as plt

plt.plot(data_x, data_y)

fig, ax = plt.subplots() #<- DEFINE FIGURE
ax.plot(data_x,data_y)
# %%
fig, ax = plt.subplots()
ax.bar(data_x,data_y)
# %%
# PLOTLY
import plotly.graph_objects as go

fig = go.Figure() #<- DEFINE FIGURE
fig.add_trace(
    go.Bar(
        x=data_x,
        y=data_y, 
        color="black"
    )
)


# %%
