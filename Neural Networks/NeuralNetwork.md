## Neural Networks

These are simplified models of the biological nervous system and therefore has drawn inspiration for the human brain.

An NN, in general, is a highly interconnected network of a large number of processing elements called neurons, in an architecture inspired by the brain. A NN can be massively parallel exhibiting parallel distributed computing.

#### Characteristics
1. Fault tolerant: Imagine if we loose few neurons in our brains, still it will not have a catastrophic impact it may cause some delay in the processing.
2. Robust: They can recall full patterns from partial, incomplete or noisy patterns.
3. Mapping capability: They can map input patterns to their associated output patterns.
4. Pattern association
5. Parallel, high speed and distributed.

#### Well known Neural network systems
1. Perceptron
2. Back propagation network
3. ADALINE(Adaptive Linear Element)
4. associative memory
5. Botlzmann machine
6. adaptive resonance theory
7. self organizing feature map
8. Hopfield network

#### Application areas already applied to
1. pattern recognition
2. image processing
3. data compression
4. forecasting
5. optimization

#### Broad classification
* single layer feed forward networks
* multilayered feed forward Networks
* recurrent networks


#### Other classification
1. Feed forward neural networks
These are the commonest type of neural network in practical applications. The first layer is the input and the last layer is the output. If there is more than one hidden layer, we call them “deep” neural networks. They compute a series of transformations that change the similarities between cases. The activities of the neurons in each layer are a non-linear function of the activities in the layer below.

2. Recurrent Networks

These have directed cycles in their connection graph. That means you can sometimes get back to where you started by following the arrows. They can have complicated dynamics and this can make them very difficult to train. They are more biologically realistic.

There is a lot of interest at present in finding efficient ways of training recurrent nets. Recurrent neural networks are a very natural way to model sequential data. They are equivalent to very deep nets with one hidden layer per time slice; except that they use the same weights at every time slice and they get input at every time slice. They have the ability to remember information in their hidden state for a long time but is very hard to train them to use this potential.

3. Symmetrically Connected Networks

These are like recurrent networks, but the connections between units are symmetrical (they have the same weight in both directions). Symmetric networks are much easier to analyze than recurrent networks. They are also more restricted in what they can do because they obey an energy function. Symmetrically connected nets without hidden units are called “Hopfield Nets.” Symmetrically connected network with hidden units are called “Boltzmann machines.”


Sources: 
https://towardsdatascience.com/the-8-neural-network-architectures-machine-learning-researchers-need-to-learn-11a0c96d6073
