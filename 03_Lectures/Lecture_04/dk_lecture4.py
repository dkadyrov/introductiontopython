#%% 
import numpy

value = numpy.random.randint(0, 100)
# %%
import numpy as np 

value = np.random.randint(0, 100)
# %%
from numpy import arange, sin 

a = arange(0, 10)
b = sin(a)
# %%
import numpy as np 

def add_sin_cos(min=0, max=10, step=11):
    array = np.linspace(min, max, step)
    x = np.sin(array)
    y = np.cos(array)
    
    return x+y

add_sin_cos(10, 20, 100)
#%%
# pip install matplotlib or pip3 install matplotlib
# pip install plotly or pip3 install plotly
# pip install pandas or pip3 install pandas

#%%
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
z = np.cos(x)

plt.plot(x, y)
plt.plot(x, z)
plt.title("Our First Graph")
plt.xlim(0, 3)
plt.ylim(0, 1)
plt.show()

# %%
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x = x,
        y = y,
        name = "Sine Wave",
        line=dict(
            color="black"
        )
    )
)
fig.add_trace(
    go.Scatter(
        x = x, 
        y = z, 
        name = "Cosine Wave"
    )
)
fig.show()
# %%
import pandas as pd

data = pd.DataFrame()
data["x"] = x 
data["y"] = y 
data["z"] = z
# %%
data.plot('x', 'y')

data.describe()

data.x.max()
data.y.min()

data["xx"] = np.arcsin(data["x"])
data["xx"] = data["xx"].replace(np.nan, 0)