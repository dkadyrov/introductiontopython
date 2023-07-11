#%%
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

train = pd.read_csv(r"titanic/train.csv")
test = pd.read_csv(r"titanic/test.csv")
#%%

example = train[["PassengerId", "Survived", "Name"]]


#%%
# %%
train["Sex_nm"] = pd.factorize(train["Sex"])[0]
train["Embarked_nm"] = pd.factorize(train["Embarked"])[0]

test["Sex_nm"] = pd.factorize(test["Sex"])[0]
test["Embarked_nm"] = pd.factorize(test["Embarked"])[0]
#%%
train = train.fillna(0)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    train[["Fare", "Sex_nm"]], train["Survived"], test_size=0.20)



#%%

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# %%


#%%
y_pred = model.predict(X_test)
# %%
testing = pd.DataFrame()
testing["y_test"] = y_test
testing["y_pred"] = y_pred
testing["check"] = testing.apply(lambda x: True if x.y_pred == x.y_test else False,  axis=1)
# %%
testing.check.value_counts()
# %%
