from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target


from sklearn.cluster import KMeans
from matplotlib import pylab as pl

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca.fit(X)
X_reduced = pca.transform(X)
print('reduced dataset shape: ', X_reduced.shape)

k_means = KMeans(n_clusters=3, random_state=0) #fixing the RNG in kmeans
k_means.fit(X)

y_pred = k_means.predict(X)

pl.scatter(X_reduced[:, 0], X_reduced[:, 1], c=y_pred, cmap='RdYlBu')

pl.show()
