#%%
import pandas as pd 
import plotly.graph_objects as go

data = pd.read_csv(r"G:\My Drive\Employment\Columbia\04_Coursework\Introduction to Python\03_Lectures\Lecture_04\titanic\train.csv")
# %%
print(data.columns)
# %%
data.Survived.value_counts()

#%%
data["Survived (String)"] = data.Survived.apply(lambda x: "Survived" if x == 1 else "Dead")
survived = data["Survived (String)"].value_counts()
#%%

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x = survived.index,
        y = survived.values
    )
)
fig.update_layout(
    title = "Titanic: Survivors",
    template="simple_white",
    yaxis=dict(
        title="Amount",
        range=[0, 600]
    ),
    xaxis=dict(
        title="Status"
    )
)
fig.write_image("survivors.jpeg")
# %%
data.corr()

fig = go.Figure()
fig.add_trace(
    go.Bar(
        x = survived.index,
        y = survived.values
    )
)
fig.update_layout(
    title = "Titanic: Survivors",
    template="simple_white",
    yaxis=dict(
        title="Amount",
        range=[0, 600]
    ),
    xaxis=dict(
        title="Status"
    )
)
#%% 
multiplier = 31.35

data["FareToday"] = data.Fare.apply(lambda x: x*multiplier)



# %%
men = data[data["Sex"] == "male"]
women = data[data["Sex"] == "female"]
women = data[data["Sex"] != "male"]

# %%
men.Pclass.value_counts()
# %%
# def set_color(value):
#     if value < 1: 
#         return "red" 
#     else: 
#         return "black"

fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x=data[data["Survived"]==0]["Age"],
        y=data[data["Survived"]==0]["Fare"],
        mode="markers", 
        marker=dict(
            color = "red"
        ),
        name="Dead"
    )
)
fig.add_trace(
    go.Scatter(
        x=data[data["Survived"]==1]["Age"],
        y=data[data["Survived"]==1]["Fare"],
        mode="markers", 
        marker=dict(
            color = "black"
        ),
        name="Survived"
    )
)

fig.update_layout(
    title="Age vs. Fare",
    yaxis=dict(
        title="Fare [$]",
        tickmode = 'linear',
        tick0 = 0,
        dtick = 50,
        range=[0, 550]
    ),
    xaxis=dict(
        title="Age",
        range=[0, 80]
    )
)
fig.show()

# %%
data["Sex_numeric"] = data["Sex"].apply(lambda x: 1 if x == "male" else 0)
#%
from sklearn.ensemble import RandomForestClassifier
##
data = data.fillna(0)

# %%
y = data["Survived"]
features = ["Pclass", "Sex_numeric", "Age", "SibSp", "Fare", "Parch", "Sex_numeric"]
x = pd.get_dummies(data[features])

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(x, y)
# %%
test = pd.read_csv(r"G:\My Drive\Employment\Columbia\04_Coursework\Introduction to Python\03_Lectures\Lecture_04\titanic\train.csv")
test["Sex_numeric"] = data["Sex"].apply(lambda x: 1 if x == "male" else 0)
test = test.fillna(0)
x_test = pd.get_dummies(test[features])
# %%

predictions = model.predict(x_test)
# %%

data.groupby("Sex").sum()
data.groupby("Sex").count()
# %%

for i, row in data.groupby("Pclass"):
    row
# %%
