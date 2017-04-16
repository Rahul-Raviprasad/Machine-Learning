from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca.fit(X)
X_reduced = pca.transform(X)
print('reduced dataset shape: ', X_reduced.shape)

import pylab as pl
pl.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y, cmap='RdYlBu')

pl.show()

print('meaning of the 2 components')
for component in pca.components_:
    print(" + ".join("%.3f x %s" % (value, name)
                     for value, name in zip(component,
                                            iris.feature_names)))
