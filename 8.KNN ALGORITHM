import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
y=iris.target

print(iris.DESCR)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state =23)
print(iris.data.shape)
print('Training set', len(x_train))
print('Test set', len(x_test))

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)

y_pred=knn.predict(x_test)
print(y_pred)

from sklearn import metrics
print("accuracy=",metrics.accuracy_score(y_pred,y_test))
from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

predicted = knn.predict(x_test)
pre_target = [iris.target_names[i] for i in predicted]
print("pre_target=", pre_target, "\n\n")
actual_target = [iris.target_names[i] for i in y_test]
print("actual_target = ", actual_target, "\n\n")
print("\t Predicted", "\t\tActual", "\t\tAnswer")
for i in range(0, len(pre_target)):
    print(i, ":", pre_target[i],"\t\t", actual_target[i],"\t\t",end='\t')
    if(pre_target[i] == actual_target[i]):
        print("Yes")
    else:
        print("No")

# pip install mlxtend

from mlxtend.plotting import plot_decision_regions
X=pd.DataFrame(iris.data)
X.columns=["Sepal_length","Sepal_Width","Petal_Length","Petal_Width"]
Y=pd.DataFrame(iris.target)
Y.columns=["Targets"]

k=1
x=X[["Petal_Width","Petal_Length"]].values
y=Y["Targets"].astype(int).values
clf=KNeighborsClassifier(n_neighbors=k)
clf.fit(x,y)
plot_decision_regions(x,y,clf=clf,legend=2)
plt.xlabel("Petal Width")
plt.ylabel("Petal Length")
plt.title(f"KNN with k={k}")
plt.show()
