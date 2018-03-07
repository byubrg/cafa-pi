from sklearn.linear_model import perceptron
import numpy as np

data = np.array([
    [0., 1.],
    [0.1, 0.9],
    [-0.1, 1.1],
    [1.0, 0.],
    [0.9, 0.1],
    [1.1, -0.1]
])
labels = np.array([
    "a",
    "a",
    "a",
    "b",
    "b",
    "b",
])

net = perceptron.Perceptron(max_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
net.fit(data, labels)

print("Prediction " + str(net.predict(data)))
print("Actual     " + str(labels))
print("Accuracy   " + str(net.score(data, labels)*100) + "%")