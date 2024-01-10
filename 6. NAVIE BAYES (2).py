import numpy as np
import pandas as pd
import sklearn

data=pd.read_csv("/content/diabetes.csv")
x=data.iloc[:,[1,2,3]].values
y=data.iloc[:,-1].values

print(data.head)

from sklearn.preprocessing import LabelEncoder

le=LabelEncoder()
x[:,0]=le.fit_transform(x[:,0])

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2, random_state=100)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
xtrain=sc.fit_transform(xtrain)
xtest=sc.fit_transform(xtest)

from sklearn.naive_bayes import GaussianNB
classifier=GaussianNB()
classifier.fit(xtrain,ytrain)
ypred=classifier.predict(xtest)

from sklearn.metrics import confusion_matrix,accuracy_score,classification_report
cm=confusion_matrix(ytest,ypred)
ac=accuracy_score(ytest,ypred)
cr=classification_report(ytest,ypred)
ac=ac*100
print(cm)
print(ac)
print(cr)
