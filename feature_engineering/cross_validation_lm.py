from sklearn.model_selection import (
    train_test_split,
    KFold,
    LeaveOneOut,
    LeavePOut,
    cross_val_score,
)
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
from statsmodels.datasets import get_rdataset

# mtcars dataset
# mtcars = get_rdataset('mtcars').data
# print("mtcars dataset:")
# print(mtcars.head())
# selected_attributes = ['mpg', 'wt']
# X = mtcars[selected_attributes]
# y = mtcars['hp']


# iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df["Target"] = iris.target_names[iris.target]
X = iris.data[:, [0, 2]]
y = iris.data[:, 1]
print("iris dataset: ")
print(iris_df)

print(" ")

# K-Fold Cross Validation
k = 6
k_fold = KFold(n_splits=k, shuffle=True, random_state=42)
linear_model = LinearRegression()
k_fold_scores = cross_val_score(
    linear_model, X, y, cv=k_fold, scoring="neg_mean_squared_error"
)
k_fold_rmse = np.sqrt(-k_fold_scores)
print(f"{k}-Fold Cross Validation :", k_fold_rmse.mean())
print(" ")

# Hold-out Validation
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
linear_model.fit(X_train, y_train)
y_pred = linear_model.predict(X_test)
holdout_rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("Hold-out Validation :", holdout_rmse)
print(" ")

# Leave One Out (LOO) Cross Validation
loo = LeaveOneOut()
linear_model = LinearRegression()
loo_scores = cross_val_score(
    linear_model, X, y, cv=loo, scoring="neg_mean_squared_error"
)
loo_rmse = np.sqrt(-loo_scores)
print("Leave One Out Cross Validation :", loo_rmse.mean())
print(" ")

# Leave P Out Cross Validation
p_out = 2
lpo = LeavePOut(p=p_out)
linear_model = LinearRegression()
lpo_scores = cross_val_score(
    linear_model, X, y, cv=lpo, scoring="neg_mean_squared_error"
)
lpo_rmse = np.sqrt(-lpo_scores)
print(f"Leave {p_out} Out Cross Validation RMSE:", lpo_rmse.mean())
print(" ")
