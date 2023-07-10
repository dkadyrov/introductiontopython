#%% 
import pandas as pd
import plotly.graph_objects as go 

btc = pd.read_csv(r"G:\My Drive\Employment\Columbia\04_Coursework\Introduction to Python\03_Lectures\Lecture_04\btc\BTC-USD.csv")

# %%
btc.head()
btc.tail()
# %%
btc["Date"] = pd.to_datetime(btc["Date"])
# %%
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=btc["Date"],
        y=btc["Open"]
    )
)
fig.add_trace(
    go.Scatter(
        x=btc["Date"], 
        y=btc["Close"]
    )
)
fig.show()
# %%