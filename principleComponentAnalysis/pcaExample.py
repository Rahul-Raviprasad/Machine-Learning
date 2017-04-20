from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target

from sklearn.decomposition import PCA

pca = PCA(n_components=2) # we want to break the data into two priciple conponent, hence n_components=2
pca.fit(X)
# The following step is going to take a four dimensional data and reduce it to 2 dimensional data.
X_reduced = pca.transform(X)
print('reduced dataset shape: ', X_reduced.shape)

import pylab as pl
pl.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, cmap='RdYlBu')

pl.show()

print('meaning of the 2 components')
# what is the meaning of these 2 new dimensions that it has tranformed into?
for component in pca.components_:
    print(" + ".join("%.3f x %s" % (value, name)
                     for value, name in zip(component,
                                            iris.feature_names)))
