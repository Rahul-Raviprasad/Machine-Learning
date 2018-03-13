# Framing: Key ML Terminology
### What is (supervised) machine learning? Concisely put, it is the following:

ML systems learn how to combine input to produce useful predictions on never-before-seen data.
Let's explore fundamental machine learning terminology.

* Labels
A label is the thing we're predicting—the y variable in simple linear regression. The label could be the future price of wheat, the kind of animal shown in a picture, the meaning of an audio clip, or just about anything.

* Features
A feature is an input variable—the x variable in simple linear regression. A simple machine learning project might use a single feature, while a more sophisticated machine learning project could use millions of features, specified as:
{x1,x2,x3,x4 ... xn}

In the spam detector example, the features could include the following:
  * words in the email text
  * sender's address
  * time of day the email was sent
  * email contains the phrase "one weird trick."

* Examples
An example is a particular instance of data, x. (We put x in boldface to indicate that it is a vector.) We break examples into two categories:
  * labeled examples
  * unlabeled examples
A labeled example includes both feature(s) and the label. That is:
labeled examples: {features, label}: (x, y)

An unlabeled example contains features but not the label. That is:

  unlabeled examples: {features, ?}: (x, ?)
Once we've trained our model with labeled examples, we use that model to predict the label on unlabeled examples. In the spam detector, unlabeled examples are new emails that humans haven't yet labeled


Models
A model defines the relationship between features and label. For example, a spam detection model might associate certain features strongly with "spam". Let's highlight two phases of a model's life:

Training means creating or learning the model. That is, you show the model labeled examples and enable the model to gradually learn the relationships between features and label.

Inference means applying the trained model to unlabeled examples. That is, you use the trained model to make useful predictions (y'). For example, during inference, you can predict medianHouseValue for new unlabeled examples.


#### Regression vs. classification
A regression model predicts continuous values. For example, regression models make predictions that answer questions like the following:

What is the value of a house in California?

What is the probability that a user will click on this ad?

A classification model predicts discrete values. For example, classification models make predictions that answer questions like the following:

Is a given email message spam or not spam?

Is this an image of a dog, a cat, or a hamster?

## Key Terms
classification model
example
feature
inference
label
model
regression
training

## Descending into ML: Linear Regression
Linear regression is a method for finding the straight line or hyperplane that best fits a set of points.

A nice first step is to examine your data by plotting it:
Applying a little algebra, you could write down this relationship as follows:

y = mx + b

where:

y: isthe value we're trying to predict.
m: is the slope of the line.
x: is the value of our input feature.
b: is the y-intercept.
By convention in machine learning, you'll write the equation for a model only slightly differently:

    y' = b + w1x1

where:

y': is the predicted label (a desired output).
b: is the bias (the y-intercept). In some machine-learning documentation, it is instead referred to as w0.
w1: is the weight of feature 1. Weight is the same concept as "slope" written with above.
x1: is a feature (a known input).

The subscripts (for example,  and ) foreshadow more sophisticated models that rely on multiple features. For example, a model that relies on three features would use the following equation:
    y' = b + w1x1 + w2x2 + w3x3

### key terms
bias
inference
linear regression
weight

## Training and Loss
Training a model simply means learning (determining) good values for all the weights and the bias from labeled examples. In supervised learning, a machine learning algorithm builds a model by examining many examples and attempting to find a model that minimizes loss; this process is called empirical risk minimization.

Loss is the penalty for a bad prediction. That is, loss is a number indicating how bad the model's prediction was on a single example. If the model's prediction is perfect, the loss is zero; otherwise, the loss is greater.
The goal of training a model is to find a set of weights and biases that have low loss, on average, across all examples

You might be wondering whether you could create a mathematical function—a loss function—that would aggregate the individual losses in a meaningful fashion.

Squared loss: a popular loss function
The linear regression models we'll examine here use a loss function called squared loss (also known as L2 loss). The squared loss for a single example is as follows:

= the square of the difference between the label and the prediction
  = (observation - prediction(x))2
  = (y - y')2

  Mean square error (MSE) is the average squared loss per example. To calculate MSE, sum up all the squared losses for individual examples and then divide by the number of examples:

Although MSE is commonly-used in machine learning, it is neither the only practical loss function nor the best loss function for all circumstances.

### Key Terms
empirical risk minimization
loss
mean squared error
squared loss
training

## Reducing Loss
To train a model, we need a good way to reduce the model’s loss. An iterative approach is one widely used method for reducing loss, and is as easy and efficient as walking down a hill.


Reducing Loss: An Iterative Approach
Iterative learning might remind you of the "Hot and Cold" kid's game for finding a hidden object like a thimble. In this game, the "hidden object" is the best possible model. You'll start with a wild guess ("The value of  is 0.") and wait for the system to tell you what the loss is. Then, you'll try another guess ("The value of  is 0.5.") and see what the loss is. Aah, you're getting warmer. Actually, if you play this game right, you'll usually be getting warmer. The real trick to the game is trying to find the best possible model as efficiently as possible.

Iterative strategies are prevalent in machine learning, primarily because they scale so well to large data sets.

The "model" takes one or more features as input and returns one prediction (y') as output. To simplify, consider a model that takes one feature and returns one prediction:

y' = b + w1x1

What initial values should we set for  and ? For linear regression problems, it turns out that the starting values aren't important. We could pick random values, but we'll just take the following trivial values instead:

 b= 0
 w1= 0
Suppose that the first feature value is 10. Plugging that feature value into the prediction function yields:

  y' = 0 + 0(10)
  y' = 0
The "Compute Loss" part of the diagram is the loss function that the model will use. Suppose we use the squared loss function. The loss function takes in two input values:

y': The model's prediction for features x
y: The correct label corresponding to features x.

It is here that the machine learning system examines the value of the loss function and generates new values for b and w1. For now, just assume that the mysterious green box devises new values and then the machine learning system re-evaluates all those features against all those labels, yielding a new value for the loss function, which yields new parameter values. And the learning continues iterating until the algorithm discovers the model parameters with the lowest possible loss. Usually, you iterate until overall loss stops changing or at least changes extremely slowly. When that happens, we say that the model has converged.

## Key Terms
convergence
loss
training

## Reducing Loss: Gradient Descent

Suppose we had the time and the computing resources to calculate the loss for all possible values of . For the kind of regression problems we've been examining, the resulting plot of loss vs.  will always be convex. In other words, the plot will always be bowl-shaped
Convex problems have only one minimum; that is, only one place where the slope is exactly 0. That minimum is where the loss function converges.

Calculating the loss function for every conceivable value of w1 over the entire data set would be an inefficient way of finding the convergence point. Let's examine a better mechanism—very popular in machine learning—called gradient descent.

The first stage in gradient descent is to pick a starting value (a starting point) for w1. The starting point doesn't matter much; therefore, many algorithms simply set w1 to 0 or pick a random value.

The gradient descent algorithm then calculates the gradient of the loss curve at the starting point. In brief, a gradient is a vector of partial derivatives; it tells you which way is "warmer" or "colder." Note that the gradient of loss with respect to a single weight is equivalent to the derivative.

Note that a gradient is a vector, so it has both of the following characteristics:

a direction
a magnitude
The gradient always points in the direction of steepest increase in the loss function. The gradient descent algorithm takes a step in the direction of the negative gradient in order to reduce loss as quickly as possible

To determine the next point along the loss function curve, the gradient descent algorithm adds some fraction of the gradient's magnitude to the starting point.

## Key Terms
gradient descent
step

## Reducing Loss: Learning Rate

As noted, the gradient vector has both a direction and a magnitude. Gradient descent algorithms multiply the gradient by a scalar known as the learning rate (also sometimes called step size) to determine the next point. For example, if the gradient magnitude is 2.5 and the learning rate is 0.01, then the gradient descent algorithm will pick the next point 0.025 away from the previous point.

Hyperparameters are the knobs that programmers tweak in machine learning algorithms. Most machine learning programmers spend a fair amount of time tuning the learning rate. If you pick a learning rate that is too small, learning will take too long

Conversely, if you specify a learning rate that is too large, the next point will perpetually bounce haphazardly across the bottom of the well like a quantum mechanics experiment gone horribly wrong:

https://en.wikipedia.org/wiki/Goldilocks_principle
There's a Goldilocks learning rate for every regression problem. The Goldilocks value is related to how flat the loss function is. If you know the gradient of the loss function is small then you can safely try a larger learning rate, which compensates for the small gradient and results in a larger step size.

The ideal learning rate in one-dimension is  1/f(x)'' (the inverse of the second derivative of f(x) at x).

The ideal learning rate for 2 or more dimensions is the inverse of the Hessian (matrix of second partial derivatives).

The story for general convex functions is more complex.

## Key Terms
hyperparameter
learning rate
step size

## Stochastic Gradient Descent

In gradient descent, a batch is the total number of examples you use to calculate the gradient in a single iteration. So far, we've assumed that the batch has been the entire data set. When working at Google scale, data sets often contain billions or even hundreds of billions of examples. Furthermore, Google data sets often contain huge numbers of features. Consequently, a batch can be enormous. A very large batch may cause even a single iteration to take a very long time to compute.

A large data set with randomly sampled examples probably contains redundant data. In fact, redundancy becomes more likely as the batch size grows. Some redundancy can be useful to smooth out noisy gradients, but enormous batches tend not to carry much more predictive value than large batches.

What if we could get the right gradient on average for much less computation? By choosing examples at random from our data set, we could estimate (albeit, noisily) a big average from a much smaller one. Stochastic gradient descent (SGD) takes this idea to the extreme--it uses only a single example (a batch size of 1) per iteration. Given enough iterations, SGD works but is very noisy. The term "stochastic" indicates that the one example comprising each batch is chosen at random.

Mini-batch stochastic gradient descent (mini-batch SGD) is a compromise between full-batch iteration and SGD. A mini-batch is typically between 10 and 1,000 examples, chosen at random. Mini-batch SGD reduces the amount of noise in SGD but is still more efficient than full-batch.

To simplify the explanation, we focused on gradient descent for a single feature. Rest assured that gradient descent also works on feature sets that contain multiple features

## Key Terms
batch
batch size
mini-batch
stochastic gradient descent

# First Steps with TensorFlow: Toolkit

The following table summarizes the purposes of the different layers:

| Toolkit(s)                         | Description         |
| :--------------------------------- | :-------------------|
| Estimator (tf.estimator)           | High-level, OOP API.|
| tf.layers/tf.losses/tf.metrics	   | Libraries for common model components.|
| TensorFlow	                       | Lower-level APIs    |

TensorFlow consists of the following two components:

a graph protocol buffer
a runtime that executes the (distributed) graph
These two components are analogous to the Java compiler and the JVM. Just as the JVM is implemented on multiple hardware platforms, so is TensorFlow—CPUs and GPUs.

Which API(s) should you use? You should use the highest level of abstraction that solves the problem. The higher levels of abstraction are easier to use, but are also (by design) less flexible. We recommend you start with the highest-level API first and get everything working. If you need additional flexibility for some special modeling concerns, move one level lower. Note that each level is built using the APIs in lower levels, so dropping down the hierarchy should be reasonably straightforward.


First Steps with TensorFlow: Toolkit
Estimated Time: 4 minutes
The following figure shows the current hierarchy of TensorFlow toolkits:

TensorFlow Estimators
tf.layers
,
tf.losses
,
tf.metrics
Python TensorFlow
C++ TensorFlow
CPU
GPU
High-level, object-oriented API
Reusable libraries for common model components
Provides Ops, which wrap C++ Kernels
Kernels work on one or more platforms
TPU
Figure 1. TensorFlow toolkit hierarchy.

The following table summarizes the purposes of the different layers:

Toolkit(s)	Description
Estimator (tf.estimator)	High-level, OOP API.
tf.layers/tf.losses/tf.metrics	Libraries for common model components.
TensorFlow	Lower-level APIs
TensorFlow consists of the following two components:

a graph protocol buffer
a runtime that executes the (distributed) graph
These two components are analogous to the Java compiler and the JVM. Just as the JVM is implemented on multiple hardware platforms, so is TensorFlow—CPUs and GPUs.

Which API(s) should you use? You should use the highest level of abstraction that solves the problem. The higher levels of abstraction are easier to use, but are also (by design) less flexible. We recommend you start with the highest-level API first and get everything working. If you need additional flexibility for some special modeling concerns, move one level lower. Note that each level is built using the APIs in lower levels, so dropping down the hierarchy should be reasonably straightforward.

#### tf.estimator API
We'll use tf.estimator for the majority of exercises in Machine Learning. Everything you'll do in the exercises could have been done in lower-level (raw) TensorFlow, but using tf.estimator dramatically lowers the number of lines of code.

tf.estimator is compatible with the scikit-learn API. Scikit-learn is an extremely popular open-source ML library in Python, with over 100k users, including many at Google.

Very broadly speaking, here's the format of a linear regression program implemented in tf.estimator:
```Python
import tensorflow as tf

# Set up a linear classifier.
classifier = tf.estimator.LinearClassifier()

# Train the model on some example data.
classifier.train(input_fn=train_input_fn, steps=2000)

# Use it to predict.
predictions = classifier.predict(input_fn=predict_input_fn)
```
## Key Terms
Estimators
graph
tensor

## perils of overfitting
William of Occam, a 14th century friar and philosopher, loved simplicity. He believed that scientists should prefer simpler formulas or theories over more complex ones. To put Occam's razor in machine learning terms:

"The less complex an ML model, the more likely that a good empirical result is not just due to the peculiarities of the sample."

A machine learning model aims to make good predictions on new, previously unseen data. But if you are building a model from your data set, how would you get the previously unseen data? Well, one way is to divide your data set into two subsets:

training set — a subset to train a model.
test set — a subset to test the model.
Good performance on the test set is a useful indicator of good performance on the new data in general, assuming that:

The test set is large enough.
You don't cheat by using the same test set over and over.
