# TensorFlow

* Open source machine learning library.
* Especially useful for deep learning.
* For research and production
* Apache 2.0 license
* its portable and scalable

tensor flow uses data in form of tensors. It can be thought of as a multidimensional array.

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
