from sklearn.model_selection import (
    train_test_split,
    KFold,
    LeaveOneOut,
    LeavePOut,
    cross_val_score,
)
from sklearn.datasets import load_iris
from sklearn.svm import SVC
import numpy as np

# load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# K-Fold Cross Validation
k_fold = KFold(n_splits=8, shuffle=True, random_state=42)
svm_model = SVC()
k_fold_scores = cross_val_score(svm_model, X, y, cv=k_fold)
# average_accuracy= np.mean(np.array(k_fold_scores.mean()))
print("K-Fold Cross Validation Scores:")
print("Mean Accuracy:", k_fold_scores.mean())
print(" ")

# Hold-out Validation
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
svm_model.fit(X_train, y_train)
holdout_accuracy = svm_model.score(X_test, y_test)
print("Hold-out Validation Accuracy:", holdout_accuracy)
print(" ")

# Leave One Out (LOO) Cross Validation
loo = LeaveOneOut()
svm_model = SVC()
loo_scores = cross_val_score(svm_model, X, y, cv=loo)
print("Leave One Out Cross Validation Scores")
print("Mean Accuracy:", loo_scores.mean())
print(" ")

# Leave P Out Cross Validation
p_out = 2  # You can change the value of p
lpo = LeavePOut(p=p_out)
svm_model = SVC()
lpo_scores = cross_val_score(svm_model, X, y, cv=lpo)
print(f"Leave {p_out} Out Cross Validation Scores:")
print("Mean Accuracy:", lpo_scores.mean())
