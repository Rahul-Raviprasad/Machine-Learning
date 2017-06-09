from sklearn import neighbors, datasets

iris = datasets.load_iris()
X, y = iris.data, iris.target

print(len(iris.data))
# create the model
knn = neighbors.KNeighborsClassifier(n_neighbors=5)

# you can do neighbors.KNeighborsClassifier? for looking at documentation

# fit the model
knn.fit(X, y)

# What kind of iris has 3cm x 5cm sepal and 4cm x 2cm petal?
# call the "predict" method:
result = knn.predict([[3, 5, 4, 2],])

print(iris.target_names[result])
# output: ['versicolor']

# You can also do probabilistic predictions also
probability = knn.predict_proba([[3, 5, 4, 2],])
print(probability)
# output: [[ 0.   0.8  0.2]]
# We can see that here there is 0% probability that it is the first flower,
# 80% probability that it is the 2nd flower and 20% probability that it is the 3rd flower.


# Plotting the output
import numpy as np
import pylab as pl
from matplotlib.colors import ListedColormap

# Create color maps for 3-class classification problem, as with iris
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

def plot_iris_knn():
    iris = datasets.load_iris()
    X = iris.data[:, :2]  # we only take the first two features. We could
                        # avoid this ugly slicing by using a two-dim dataset
    y = iris.target

    knn = neighbors.KNeighborsClassifier(n_neighbors=3)
    knn.fit(X, y)

    x_min, x_max = X[:, 0].min() - .1, X[:, 0].max() + .1
    y_min, y_max = X[:, 1].min() - .1, X[:, 1].max() + .1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    pl.figure()
    pl.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    pl.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
    pl.xlabel('sepal length (cm)')
    pl.ylabel('sepal width (cm)')
    pl.axis('tight')
    pl.show()

plot_iris_knn()
