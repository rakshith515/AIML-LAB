import numpy as np

X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
Y = np.array(([92], [86], [89]), dtype=float)
X = X / np.amax(X, axis=0)
actual_output = Y / 100
print(X)
print(actual_output)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def derivatives_sigmoid(x):
    return x * (1 - x)

epoch = 1000
learning_rate = 0.15
inputlayer_neurons = 2
hiddenlayer_neurons = 3
outputlayer_neurons = 1

wh = np.random.uniform(low=-0.05, high=0.05, size=(inputlayer_neurons, hiddenlayer_neurons))
bh = np.random.uniform(low=-0.05, high=0.05, size=(1, hiddenlayer_neurons))
wo = np.random.uniform(low=-0.05, high=0.05, size=(hiddenlayer_neurons, outputlayer_neurons))
bo = np.random.uniform(low=-0.05, high=0.05, size=(1, outputlayer_neurons))

for i in range(epoch):
    net_h = np.dot(X, wh) + bh
    sigma_h = sigmoid(net_h)
    net_o = np.dot(sigma_h, wo) + bo
    output = sigmoid(net_o)

    eo = actual_output - output
    outgrad = derivatives_sigmoid(output)
    d_output = eo * outgrad

    eh = d_output.dot(wo.T)
    hiddengrad = derivatives_sigmoid(sigma_h)
    d_hidden = eh * hiddengrad

    wo += sigma_h.T.dot(d_output) * learning_rate
    wh += X.T.dot(d_hidden) * learning_rate

    # sum_error = 0

    # for j in range(len(actual_output)):
    #     print(output[j], actual_output[j])
    #     sum_error += ((output[j] - actual_output[j]) ** 2)
    # sum_error /= 2

    # print(f'Epoch {i} error {sum_error}')

print("Normalized Input: \n" + str(X))
print("Actual Output: \n" + str(actual_output))
print("Predicted Output: \n", output)
