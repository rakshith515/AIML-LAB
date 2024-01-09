import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB

data = pd.read_csv('/content/diabetes.csv')
print("The first 5 Values of data is :\n", data.head())

# obtain train data and train output
X = data.iloc[:, :-1]
print("\nThe First 5 values of the train data is\n", X.head())

y = data.iloc[:, -1]
print("\nThe First 5 values of train output is\n", y.head())

# convert them in numbers
le_pregnancies = LabelEncoder()
X.Pregnancies = le_pregnancies.fit_transform(X.Pregnancies)

le_glucose = LabelEncoder()
X.Glucose = le_glucose.fit_transform(X.Glucose)

le_BloodPressure = LabelEncoder()
X.BloodPressure = le_BloodPressure.fit_transform(X.BloodPressure)

le_SkinThickness = LabelEncoder()
X.SkinThickness = le_SkinThickness.fit_transform(X.SkinThickness)

le_Insulin = LabelEncoder()
X.Insulin = le_Insulin.fit_transform(X.Insulin)

le_BMI = LabelEncoder()
X.BMI = le_BMI.fit_transform(X.BMI)

le_DiabetesPedigreeFunction = LabelEncoder()
X.DiabetesPedigreeFunction = le_DiabetesPedigreeFunction.fit_transform(X.DiabetesPedigreeFunction)

le_Age = LabelEncoder()
X.Age = le_Age.fit_transform(X.Age)


print("\nNow the Train output is\n", X.head())

le_outcome = LabelEncoder()
y = le_outcome.fit_transform(y)
print("\nNow the Train output is\n",y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.20)

classifier = GaussianNB()
classifier.fit(X_train, y_train)
pred = classifier.predict(X_test)
from sklearn.metrics import accuracy_score,confusion_matrix
print("Accuracy is:", accuracy_score(pred, y_test))
print("Confusion Matrix : \n", confusion_matrix(pred, y_test))
