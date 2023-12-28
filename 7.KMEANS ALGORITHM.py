import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.cluster import KMeans
import sklearn.metrics as sm
import pandas as pd
import numpy as np

iris = datasets.load_iris()
print(iris)
print("\n IRIS DATA : ",iris.data)
print("\n IRIS FEATURES : \n",iris.feature_names)
print("\n IRIS TARGET : \n",iris.target)
print("\n IRIS TARGET NAMES : \n",iris.target_names)

X = pd.DataFrame(iris.data)
print(X)
X.columns = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width']
y = pd.DataFrame(iris.target)
y.columns = ['Targets']

plt.figure(figsize = (14,7))
colormap = np.array(['red', 'lime', 'black'])
plt.subplot(1,2,1)
plt.scatter(X.Sepal_Length,X.Sepal_Width,c=colormap[y.Targets],s=40)
plt.title = ("Sepal")
colormap1 = np.array(['blue', 'yellow', 'pink'])
plt.subplot(1,2,2)
plt.scatter(X.Petal_Length,X.Petal_Width,c=colormap1[y.Targets],s=40)
plt.title = ("Petal")

model1 = KMeans(n_clusters=3,random_state=100)
model1.fit(X)
Y_pred = model1.labels_
print(Y_pred)

from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture 

gnm = GaussianMixture(n_components = 3,covariance_type = "full",random_state = 100)
gnm.fit(X)
y_cluster_gnm = gnm.predict(X)
y_cluster_gnm

plt.figure(figsize = (14,7))
colormap1 = np.array(['blue', 'yellow', 'pink'])
plt.subplot(1,3,1)
plt.scatter(X.Petal_Length,X.Petal_Width,c=colormap1[y.Targets],s=20)
plt.title = ("Real Classification")
colormap = np.array(['red', 'lime', 'black'])
plt.subplot(1,3,2)
plt.scatter(X.Petal_Length,X.Petal_Width,c=colormap[y_cluster_gnm],s=20)
plt.title = ("GNM Classification")
colormap1 = np.array(['blue', 'yellow', 'pink'])
plt.subplot(1,3,3)
plt.scatter(X.Petal_Length,X.Petal_Width,c=colormap1[Y_pred],s=40)
plt.title = ("KMEANS CLUSTERING")


print("GNM ACCURACY")
print("ACCURACY",sm.accuracy_score(y,y_cluster_gnm))
print("CONFUSION MATRIX : \n",sm.confusion_matrix(y,y_cluster_gnm))
