# TensorFlow

### Features
* Open source machine learning library.
* Especially useful for deep learning.
* For research and production
* Apache 2.0 license
* Its portable and scalable

Tensor flow uses data in form of tensors. It can be thought of as a multidimensional array.
Tensor flow models generally take tensors as input and give us tensor as output.

## What is a Tensor?
One of the best explanations for beginners is given by Dan Fleisch here
https://www.youtube.com/watch?v=f5liqUk0ZTw

## Data Flow graphs
Computation is defined as a directed acyclic graph (DAG) to optimize an objective function
* Graph is defined in high level language (Python, Go, C++)
* graph is compiled and optimized
* graph is executed (in parts or fully) on available low level devices(CPU, GPU).
* Data (tensors) flows through the graph
* TensorFlow can compute gradients automatically.

## Architecture
* Core in C++
* Different frontends
  * Python and C++ today community might add more.

## Models in tensor flow
* Inception
https://github.com/tensorflow/models/tree/master/research/inception
* Show and tell: A neural Image caption generator.
https://github.com/tensorflow/models/tree/master/research/im2txt
* Language model on one billion word
https://github.com/tensorflow/models/tree/master/research/lm_1b
* SyntaxNet: Neural Models of syntax
https://github.com/tensorflow/models/tree/master/research/syntaxnet
* resnet on cifar10 and cifar100
https://github.com/tensorflow/models/tree/master/research/resnet
* sequence to sequence with attention model for text summarization
https://github.com/tensorflow/models/tree/master/research/textsum
* tensorflow slim image classification library
https://github.com/tensorflow/models/tree/master/research/slim
* Image compression with neural networks
https://github.com/tensorflow/models/tree/master/research/compression
* Autoencoders
https://github.com/tensorflow/models/tree/master/research/autoencoder
* Swivel
https://github.com/tensorflow/models/tree/master/research/swivel
* Spatial transformer network
https://github.com/tensorflow/models/tree/master/research/transformer

## Solving a linear regression problem
what we are trying to do?
Mystery Equation: y = 0.1 * x + 0.3 + noise
Model: y = W * x + b
Objective:
give enough (x,y) value samples, figure out the value of W and b.

## Solving MNIST problem
Given enough images and labels, figure out the weights and biases so that the model can correctly identify the digits.

## Exercises to run
1. Run all the cells
2. Uncomment the graph writing to see what the graph looks like.
3. Print out loss value every 100 steps. What do you notice?
4. Save checkpoint every 500 steps
5. Run evaluation with different checkpoints. What do you notice?
6. Run evaluation on the complete validation set.
7. Build evaluation graph from scratch instead of importing from meta graph.
