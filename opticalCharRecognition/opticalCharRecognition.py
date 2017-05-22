from sklearn import datasets
digits = datasets.load_digits()
digits.images.shape

import matplotlib.pyplot as plt

# plotting few of these

fig, axes = plt.subplots(10, 10, figsize=(8, 8))
fig.subplots_adjust(hspace=0.1, wspace=0.1)

for i, ax in enumerate(axes.flat):
    ax.imshow(digits.images[i], cmap='binary')
    ax.text(0.05, 0.05, str(digits.target[i]), transform=ax.transAxes, color='green')
    ax.set_xticks([])
    ax.set_yticks([])

# The images themselves
print(digits.images.shape)
print(digits.images[0])


# The data for use in our algorithms
print(digits.data.shape)
print(digits.data[0])

# The target label
print(digits.target)

# Unsupervised Learning: Dimensionality Reduction

from sklearn.manifold import Isomap

iso = Isomap(n_components=2)
data_projected = iso.fit_transform(digits.data)


data_projected.shape



plt.scatter(data_projected[:, 0], data_projected[:, 1], c=digits.target, edgecolor='none', alpha=0.5, cmap=plt.cm.get_cmap('nipy_spectral', 10));
plt.colorbar(label='digit label', ticks=range(10))
plt.clim(-0.5, 9.5)

# We see here that the digits are fairly well-separated in the parameter space; this tells us that a supervised classification algorithm should perform fairly well. Let's give it a try.


# classification on digits

# split into test and train data
from sklearn.cross_validation import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(digits.data, digits.target,
                                                random_state=2)
print(Xtrain.shape, Xtest.shape)

# Let's use a simple logistic regression which (despite its confusing name) is a classification algorithm:

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(penalty='l2')
clf.fit(Xtrain, ytrain)
ypred = clf.predict(Xtest)


from sklearn.metrics import accuracy_score
accuracy_score(ytest, ypred)

from sklearn.metrics import confusion_matrix
print(confusion_matrix(ytest, ypred))

plt.imshow(np.log(confusion_matrix(ytest, ypred)),
           cmap='Blues', interpolation='nearest')
plt.grid(False)
plt.ylabel('true')
plt.xlabel('predicted');

# We might also take a look at some of the outputs along with their predicted labels. We'll make the bad labels red:

fig, axes = plt.subplots(10, 10, figsize=(8, 8))
fig.subplots_adjust(hspace=0.1, wspace=0.1)

for i, ax in enumerate(axes.flat):
    ax.imshow(Xtest[i].reshape(8, 8), cmap='binary')
    ax.text(0.05, 0.05, str(ypred[i]),
            transform=ax.transAxes,
            color='green' if (ytest[i] == ypred[i]) else 'red')
    ax.set_xticks([])
    ax.set_yticks([])

plt.show()
