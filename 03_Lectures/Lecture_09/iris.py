#%%
import pandas as pd

data = pd.read_csv("Iris.csv")
# %%
import plotly.graph_objects as go

data["Species_num"] = pd.factorize(data["Species"])[0]
data["Color"] = data["Species_num"].apply(lambda x: "red" if x==1 else ("blue" if x==0 else "green"))

color = {
    0: "blue",
    1: "red",
    2: "green"
}

#%%
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x= data["SepalLengthCm"],
        y= data["SepalWidthCm"],
        mode="markers",
        marker=dict(
            color=data["Color"]
        )
    )
)
fig.update_layout(
    xaxis_title="Sepal Length",
    yaxis_title="Sepal Width"
)
fig.show()

#%%
fig = go.Figure()
fig.add_trace(
    go.Scatter(
        x= data["PetalLengthCm"],
        y= data["PetalWidthCm"],
        mode="markers",
        marker=dict(
            color=data["Color"]
        )
    )
)
fig.update_layout(
    xaxis_title="Petal Length",
    yaxis_title="Petal Width"
)
fig.show()



#%%
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    data[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]], data["Species_num"], test_size=0.20) 

# %%
from sklearn.neighbors import KNeighborsClassifier



for n in range(1,10): 
    classifier = KNeighborsClassifier(n_neighbors=n)
    classifier.fit(X_train, y_train) 

    y_predict = classifier.predict(X_test)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x= data["SepalLengthCm"],
            y= data["SepalWidthCm"],
            mode="markers",
            marker=dict(
                color=data["Color"]
            )
        )
    )
    fig.add_trace(
        go.Scatter(
            x=X_test["SepalLengthCm"],
            y=X_test["SepalWidthCm"],
            mode="markers", 
            marker=dict(
                color=[color[i] for i in y_predict],
                line=dict(
                    width=2
                )
            )
        )
    )

    fig.update_layout(
        title=f"KNN with {n}",
        xaxis_title="Sepal Length",
        yaxis_title="Sepal Width"
    )
    fig.show()

# %%
from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, y_predict))
print(classification_report(y_test, y_predict)) 