from sklearn import neighbors, datasets

iris = datasets.load_iris()
X, y = iris.data, iris.target

# create the model
knn = neighbors.KNeighborsClassifier(n_neighbors=5)

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
