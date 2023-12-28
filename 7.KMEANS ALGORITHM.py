import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import datasets
import sklearn.metrics as sm
from sklearn.mixture import GaussianMixture
from scipy.stats import mode

iris = datasets.load_iris()
X = pd.DataFrame(iris.data)
Y = pd.DataFrame(iris.target)

X.columns = ['Sepal_Length', 'Sepal_Width', 'Petal_Length', 'Petal_Width']
Y.columns = ['Targets']

import matplotlib.pyplot as plt

plt.figure(figsize=(14, 7))
colormap = np.array(['red', 'lime', 'black'])
plt.subplot(1, 2, 1)
plt.scatter(X.Sepal_Length, X.Sepal_Width, c=colormap[Y.Targets], s=40)
plt.title('SEPAL')
plt.subplot(1, 2, 2)
plt.scatter(X.Petal_Length, X.Petal_Width, c=colormap[Y.Targets], s=40)
plt.title('PETAL')

gnm = GaussianMixture(n_components=3, covariance_type="full", random_state=100)
gnm.fit(X)
labels = gnm.predict(X)

kmeans = KMeans(n_clusters=3, random_state=100)
kmeans.fit(X)
y_pred = kmeans.labels_


# Print the accuracy of each model
print("Gaussian Mixtures Accuracy: ", sm.accuracy_score(Y, labels))
print("K-means Accuracy: ", sm.accuracy_score(Y, y_pred))

# Print the confusion matrix of each model
print("\nConfusion Matrix for Gaussian Mixture Models:\n")
print(sm.confusion_matrix(Y, labels))
print("\nConfusion Matrix for K-means Model:\n")
print(sm.confusion_matrix(Y, y_pred))

plt.figure(figsize = (14,7))
colormap1 = np.array(['blue', 'yellow', 'pink'])
plt.subplot(1,3,1)
plt.scatter(X.Petal_Length,X.Petal_Width,c=colormap1[Y.Targets],s=20)
plt.title = ("Real Classification")
colormap = np.array(['red', 'lime', 'black'])
plt.subplot(1,3,2)
plt.scatter(X.Petal_Length,X.Petal_Width,c=colormap[labels],s=20)
plt.title = ("GNM Classification")
colormap1 = np.array(['blue', 'yellow', 'pink'])
plt.subplot(1,3,3)
plt.scatter(X.Petal_Length,X.Petal_Width,c=colormap1[y_pred],s=40)
plt.title = ("KMEANS CLUSTERING")
