#%%
import pandas as pd
from astrology import astrological_sign 

data = pd.read_excel(r"G:\My Drive\Employment\Columbia\04_Coursework\Introduction to Python\01_Admin\Columbia Student Form.xlsx")
# %%
df = pd.DataFrame()
df["birthday"] = data["Birthday"] 
df["color"] = data["Favorite Color"]
df["OS"] = data["What operating system (OS) are you using for class?"]
df["languages"] = data["How many languages do you speak? "] 
df["animal"] = data["Dogs, Cats, or other"]
df["superpower"] = data["What superpower would you rather have? Flight or Invisibility? "]
df["weather"] = data["Would you rather be in hot weather or cold weather? "]
df["travel"] = data["Would you rather travel into the past or into the future? "]
# %%
import datetime

today = datetime.datetime.today()
# %%
df["age"] = today - df["birthday"]
# %%
df["age_years"] = df["age"].dt.days / (365.25)
# %%
df["years"] = round(df["age_years"], 2)
# %%
df.color = df.color.str.strip()
df.color = df.color.str.title()
# %%
df.OS = df.OS.replace("PC sometimes iOS", "PC")
# %%
# Sign 
df["sign"] = df["birthday"].apply(lambda x: astrological_sign(x.month, x.day))

#%%
df["animal"] = df["animal"].replace("I don't have any pets", "None")
#%%
df.corr()

#%%
df["superpower_int"] = pd.factorize(df['superpower'])[0]
df["color_int"] = pd.factorize(df['color'])[0]
df["OS_int"] = pd.factorize(df['OS'])[0]
df["animal_int"] = pd.factorize(df['animal'])[0]
df["weather_int"] = pd.factorize(df['weather'])[0]
df["travel_int"] = pd.factorize(df['travel'])[0]
df["sign_int"] = pd.factorize(df['sign'])[0]
#%%
import matplotlib.pyplot as plt

plt.plot(df["sign"], df["color"], "o")
#%%
import matplotlib.pyplot as plt

plt.matshow(df.corr())
plt.show()

# Information on dealing python environments
# How to download from my github as well as yours
# Upload files to canvas
# 
# %%
def heatmap(x, y, size):
    fig, ax = plt.subplots()
    
    # Mapping from column names to integer coordinates
    x_labels = [v for v in sorted(x.unique())]
    y_labels = [v for v in sorted(y.unique())]
    x_to_num = {p[1]:p[0] for p in enumerate(x_labels)} 
    y_to_num = {p[1]:p[0] for p in enumerate(y_labels)} 
    
    size_scale = 500
    ax.scatter(
        x=x.map(x_to_num), # Use mapping for x
        y=y.map(y_to_num), # Use mapping for y
        s=size * size_scale, # Vector of square sizes, proportional to size parameter
        marker='s' # Use square as scatterplot marker
    )
    
    # Show column labels on the axes
    ax.set_xticks([x_to_num[v] for v in x_labels])
    ax.set_xticklabels(x_labels, rotation=45, horizontalalignment='right')
    ax.set_yticks([y_to_num[v] for v in y_labels])
    ax.set_yticklabels(y_labels)
    

corr = df.corr()
corr = pd.melt(corr.reset_index(), id_vars='index') # Unpivot the dataframe, so we can get pair of arrays for x and y
corr.columns = ['x', 'y', 'value']
heatmap(
    x=corr['x'],
    y=corr['y'],
    size=corr['value'].abs()
)
# %%
pd.plotting.scatter_matrix(df, alpha=0.2)
# %%
df.plot.scatter_matrix()
#%%
import matplotlib.pyplot as plt

plt.plot(df["sign"], df["color"], "o")


# %%
fig, ax = plt.subplots()
ax.scatter(df["sign"], df["OS"])
ax.scatter(df["sign"], df["color"])

# %%
plt.plot(df["travel"], df["years"], "o")
# %%
