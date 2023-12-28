filename = 'pima-indians-diabetes.csv'
import pandas as pd
import numpy as np
df = pd.read_csv(filename)
df = df.astype(float)
train = df.sample(frac=0.8,random_state=105)
test = df.drop(train.index)

df.describe()
df.info()

df.hist(bins=30,figsize=(15,10))

print(len(train),len(test))

outcome_group = train.groupby(df.columns[-1])
n_attr = len(df.columns)-1
summaries = {}
for classValue,instances in outcome_group:
    attr_mv = []
    mean = list(instances.mean(axis=0).values)
    stdev = list(instances.std(axis=0).values)
# print(f"Class : {classValue}\n mean : )
    for i in range(n_attr):
        attr_mv.append([mean[i],stdev[i]])

    summaries[classValue]=attr_mv
print(summaries)


import math
def calculateProb(x, mean, stdev):
    exponent = math.exp(-math.pow(x-mean,2)/(2*math.pow(stdev,2)))
    return (1 / (math.sqrt(2*math.pi)*math.pow(stdev,2))) * exponent

def calculateClassProb(summaries, X_vec):
    probabilities = {}
    for classValue, classSummaries in summaries.items():
        probabilities[classValue] = 1
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            x = X_vec[i]
            probabilities[classValue] *= calculateProb(x, mean, stdev)

    return probabilities

def predict(summaries, X_vec):
    prob = calculateClassProb(summaries, X_vec)
    bestLabel, bestProb = None, -1
    for classValue, probability in prob.items():
        if bestLabel is None or probability > bestProb:
            bestProb = probability
            bestLabel = classValue
    return bestLabel


predictions = []
testSet = test.values.tolist()
for i in range(len(testSet)):
    result = predict(summaries,testSet[i])
    predictions.append(result)


def getAccuracy(test, predictions):
    correct = 0
    for i in range(len(test)):
        if test.iloc[i,-1] == predictions[i]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0
accuracy = getAccuracy(test, predictions)
print(f'Split {len(df)} rows into train={len(train)} and test={len(test)}')
print(f'Accuracy: {accuracy}')

