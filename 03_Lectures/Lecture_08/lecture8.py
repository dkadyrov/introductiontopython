"""
[0,2] and [2, 5]

y = mx + b 

2 = m(0) + b 
b = 2 

5 = m(2) + 2 
m = (5-2)/2 = 1.5

y = 1.5x + 2
"""
#%%
import pandas as pd
import numpy as np 

df = pd.DataFrame()
df["x"] = np.linspace(0, 10, 1000)
df["y"] = 1.5 * df["x"] + 2
df["y_random"] = df["y"] + np.random.normal(0, 1, 1000)
# %%
import plotly.graph_objects as go


# %%
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(df[["x"]], df["y_random"])

#%%
df["y_fit"] = model.predict(df[["x"]])

model.coef_
model.intercept_


# %%
prediction = pd.DataFrame()
prediction["x"] = np.linspace(0, 100, 1000)
prediction["y"] = model.predict(prediction[["x"]])
prediction["alt_y"] = model.coef_[0] * prediction["x"] + model.intercept_
# %%
# %%
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=df["x"],
        y=df["y"],
        mode="lines",
        name="y = 1.5x + 2"
    )
)
fig.add_trace(
    go.Scatter(
        x=df["x"],
        y=df["y_random"],
        mode="markers",
        name="y = 1.5x + 2 + noise"
    )
)
fig.add_trace(
    go.Scatter(
        x=df["x"],
        y=df["y_fit"],
        mode="lines",
        name="fitted_function"
    )
)
fig.add_trace(
    go.Scatter(
        x=prediction["x"],
        y=prediction["y"],
        mode="lines",
        name="extended_function"
    )
)

fig.show()
# %%
# training 80%
# testing 20%

# training 80%
# validation 10%
# testing 10%

df = pd.DataFrame()
df["x"] = np.linspace(0, 3*np.pi, 1000)
df["y"] = np.sin(df.x)
df["y_noise"] = np.sin(df.x) + np.random.normal(0, 0.1, 1000)
# %%

# %%
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x = df["x"],
        y = df["y"],
        name="base"
    )
)
fig.add_trace(
    go.Scatter(
        x = df["x"],
        y = df["y_noise"],
        name = "noise"
    )
)

for i in range(1, 6):
    train_x = df.x.iloc[0:int(len(df)*.8)]
    train_y = df.y_noise.iloc[0:int(len(df)*.8)]
    poly = PolynomialFeatures(i, include_bias=False)
    poly_features = poly.fit_transform(train_x.values.reshape(-1,1))

    model = LinearRegression()
    model.fit(poly_features, train_y)

    df["predicted"] = model.predict(poly.fit_transform(df.x.values.reshape(-1,1)))

    error = mean_squared_error(df["y"], df["predicted"])

    fig.add_trace(
        go.Scatter(
            x = df["x"],
            y = df["predicted"],
            name = f"predicted {i} - {error}"
        )
    )
fig
# %%
## y = mx+b 
## y = ax^2 + bx + c 
## y = ax^3 + bx^2 + cx + d 

#%%
# Curve fitting

