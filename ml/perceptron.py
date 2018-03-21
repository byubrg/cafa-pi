from sklearn.linear_model import perceptron
import numpy as np
import pandas as pd
import embeddings

data, labels = embeddings.load_data_discrete("../data/example/train_fake.csv")

data = [np.array(row).flatten() for row in data]

net = perceptron.Perceptron(max_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
net.fit(data, labels)

print("Prediction " + str(net.predict(data)))
print("Actual     " + str(labels))
print("Accuracy   " + str(net.score(data, labels)*100) + "%")