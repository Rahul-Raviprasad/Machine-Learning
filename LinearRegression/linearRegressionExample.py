import numpy as np
import matplotlib.pyplot as plt

# Every algorithm is exposed in scikit-learn via an ''Estimator'' object.
# For instance a linear regression is implemented as an Estimator object.
# for more read: http://scikit-learn.org/stable/tutorial/statistical_inference/settings.html
from sklearn.linear_model import LinearRegression


model = LinearRegression(normalize=True)

# check if parameter is set
print(model.normalize)

# we can see what parameters are set and defaulted to.
print(model)

# Step : getting the data
#  Instead of getting the data from some source, we are going to be genrating the data using numpy
# this is just some data generated through our function
x = np.arange(10)
y = 3 * x + 1
print(x)
print(y)

plt.plot(x, y, 'o')

plt.show()

# The input data for sklearn is 2D: (samples == 3 x features == 1)
X = x[:, np.newaxis] # making our x data to be 2D for sklearn
print(X)
print(y)

##------------------------------------------

# ML Step
# now that we have data in the form we need we need to fit the model with the data.
model.fit(X,y)

# Underscore at the end indicate a fit parameter
print(model.coef_)
# output: [ 3.]
print(model.intercept_)
# output: 1.0
# The output are obvious since we made the data in that way only, but had we been just given the matrix/array
# we would have figured the linear line out from it.
