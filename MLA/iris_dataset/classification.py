
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier, StackingClassifier
from sklearn.svm import SVC
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from utility import evaluation

# iris dataset: input and label
iris = datasets.load_iris()
X = iris.data
y = iris.target

# split dataset: training and testing 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

# classifiers dictionary 
classifiers = {
    "SVM": SVC(kernel='rbf', C=1.0, random_state=123),
    "SGD": SGDClassifier(loss='log', random_state=123),
    "KNN": KNeighborsClassifier(n_neighbors=3),
    "Gaussian Processes": GaussianProcessClassifier(1.0 * RBF(1.0)),
    "Decision Trees": DecisionTreeClassifier(max_depth=5, random_state=123)
}

# model fitting and evalution
evaluation_metrics = {}
for name, model in classifiers.items():

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    print("--------------------",name,"--------------------")
    accuracy = evaluation(y_test,y_pred,iris.target_names)
    evaluation_metrics[name] = accuracy

# select top 4 classifiers
models = sorted(classifiers.keys(), key=lambda x: evaluation_metrics[x], reverse=True)
top_models = models[:4]

print("Top 4 models : ",top_models)
# ensemble techniques (bagging, boosting, stacking): top 4 models
ensemble_models = {
    "Bagging": BaggingClassifier(base_estimator=None, n_estimators=10, random_state=123),
    "AdaBoost": AdaBoostClassifier(n_estimators=50, random_state=123),
    "Stacking": StackingClassifier(estimators=[(name, classifiers[name]) for name in top_models], final_estimator=None, cv=5)
}

#using ensemble model
for name, model in ensemble_models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    print("--------------------",name,"--------------------")
    accuracy = evaluation(y_test,y_pred,iris.target_names)

  

