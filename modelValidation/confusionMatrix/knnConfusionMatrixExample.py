from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
from sklearn.neighbors import KNeighborsClassifier

X, y = iris.data, iris.target

classifier = KNeighborsClassifier(n_neighbors=1)

# Bad approach: training on entire data, and not splitting it into test and train data
classifier.fit(X, y)
y_predicted = classifier.predict(X)

print(np.all(y == y_predicted)) # getting True as expected, since the train and test data is same.

# Using the confusion matrix
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y, y_predicted))

# For each class, all 50 training samples are correctly identified.
# But this does not mean that our model is perfect!
# In particular, such a model generalizes extremely poorly to new data.
# We can simulate this by splitting our data into a training set and a testing set.

from sklearn.cross_validation import train_test_split

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y)
classifier.fit(Xtrain, ytrain)
y_predicted = classifier.predict(Xtest)
print(confusion_matrix(ytest, y_predicted))

# This paints a better picture of the true performance of our classifier:
# apparently there is some confusion between the second and third species
