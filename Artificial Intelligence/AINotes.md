# Artificial Intelligence
Generating or building model that can think, solve a problem etc.

Generate and test

## Reasoning: Goal Trees and problem solving

### Modeling problem solving
  * generate and test
  * problem reduction

### problem reduction tree
### transforms + example
### reflections

* Knowledge is power
* Catechism
  * what kind
  * how represented
  * how used
  * how much

* Catechism is knowledge about knowledge, which gives you the real power.
for eg. solving integral 2x dx is will require a transformation of moving constant terms out of the integral and hence transforming into a simpler problem to solve is the knowledge catechism is talking about.

We need to understand how we generally solve a problem.

Lets see how to solve an integral

We will have a basic table of integrations we can solve directly.
Now we don't have a table with this exact integral solution. we need to move from this point of problem to another which is simpler to solve. these kind of transformation we regularly do for solving mathematical problems.
This going from one point to another * ---> * , is called problem reduction

Safe transformation
Heuristic transformations


When we draw out how we are going to solve a problem, by problem reduction and we draw out the tree and how we can travel from one node to another.
Then that tree is called a Problem reduction tree, Goal tree or a AND/OR tree.

Curious findings about the integral solving program written so long ago
1. it was able to solve 52 out 54 complicated integrations problem
2. the worst case depth was 7
3. average depth of the tree was only 3 (tells us why most humans can do integrations reasonably well)
4. unused branches on most problems was around 1 (implies the tree didn't branch out that much, so a decision to take a different route would not be very costly.)
5. how much knowledge required to do well on a integration exam also was somewhat small. around 26 equations for knowledge table (i.e solving basic equations), ~12 hueristic transformations, and ~12 safe transformations

## Reasoning: Goal Trees and Rule based expert systems

* Simon's ant

complexity of behavior C(behavior) = max( C(program), C(environment))

the ant had a complex path back to its home, because it was trying to avoid the pebbles and stones, not because the logic(program) to go home was complex.
* engineering yourself
  specific cases


### Forward chaining rule based "Expert" system
not really expert, but based on certain rules we come to conclusion. Like if we an say in a zoo with 100s of animals and are given information like,
 1. has hair -> must be a mammal
 2. has claw, sharp teeth, forward pointing eye ---AND Gate(all must be true)---> must be a carnivore
 3. mammal + carnivore + has spots + very fast --- AND Gate --> must be a cheetah.

 So based on these rules we were able to identify a cheetah.
even the above can be written as a goal tree, and it will able to answer questions about its decisions by moving up and down the tree.
for example : Why is this animal a cheetah?? --> (move up the tree) because it has spots, is mammal and carnivore // Why is it a carnivore? because it eats meat, has sharp teeth and forward pointing eyes and so on.

Instead of moving forward with facts, we can also move backwards on a hypothesis. like are we really looking at a cheetah?


#### problems
there rule based systems lack what we call common sense. Why should be place squishy items on the top of a grocery bag.

### Search: Depth first, hill climbing, beam

British Museum approach: find every possible path. no backtracking since we find all paths.
Depth first approach: we move down the left node and keep searching and if we don't find then backtrack to the node where we made the last decision and take that branch and repeat until we find it.
breadth first approach: similar to breadth first, but we check at each level
hill climbing: if you have information you are getting close to your goal then use it.
beam search: give a beam width

###  The best path instead of a good path
* oracle
* branch and bound
* + Extended list enqueued list
* + Admissible heuristics
* A*

using enqueued lists helps with both depth first and breadth first search. improves the efficiency.


Search is not equal to maps, it is about the choice you make, the decisions you come up with.

### Search: Games, Minimax and Alpha Beta

ways to play
Minimax
alpha-beta
progressive deepening
deep blue = minimax + alpha beta + progressive deepening + parallel computing + opening book + end game + uneven tree development

dead horse principle
Marshall arts principle
Anytime algorithms

### Constraints: Interpreting Line Drawings

Rumplestilskin principle
godlilocks principle
power of correlation

### Introduction to Learning, nearest neighbor
* Regularity
  * boosting
  * nearest neighbor
  * neural nets
* Constraint
  * one shor
  * explanation based learning

## Learning: Identification Trees, Disorder
  * identification Trees:
  - you can have a bunch of tests and conduct them which can identify, each of the tests can pose some challenges like it could be costly.
  some test might then require follow up test, which can make them look like a tree.
  - tests which produce more homogenous sets are better than those that give mixed output.
  - sometime we will not find test which will help us to clearly tell if it will produce homogenous result. So we will try to determine the Disorder in a set
  - Quality of a test is equal to  on sum of all disorder of sets times the number of samples in set divided by the number of samples handed by the test.
  - this q has to be as small as possible.
  - good identification trees are as small as possible.

  * measuring disorder
  * rules
  * simplification of rules

## Neural Nets
* Models of problem solving
* Modes of Learning: basic biology inspired
* neural nets
  naive neurobiology
  hill climbing
  threshold trick
  sigmoid trick
  world's simplest net problems
## Deep neural nets
  * old days
  * convolution
  * pooling
  * sigmoid/logistic output
  * Auto coding
  * fooling
  * soft max
  * dropout

## Learning: Genetic Algorithms
* naive evolution: mitosis in reproduction
* mimicking
* choices abound
* fitness space
* examples  

## Learning: Sparse Spaces, Phonology
* what if god were an engineer
* yip-sussman machine/learner
* reflections

Phonology: when a person makes a sound then it is heard by another and processed as a sequence of distinctive feature vectors. human can have about 16000 distinctive such sounds, there are no languages which has more than hundred.

## Learning: Near Misses, Felicity Conditions
* you can't learn unless you almost know already
* value of talking to yourself

## Learning: Support Vector Machines
* decision boundaries
* widest street approach
* kernel functions
* history lesson

## Learning: Boosting
it has to do with binary classification
* weak-strong: any classifier would have an error rate, which will range from zero to one. near 0 will be strong classifiers and near say 0.5 are weak classifier, near 1 are useless
* Ada boost
* overfitting
* decision tree stumps

boosting can be used with any classifier

there is no clear explanation yet why boosting doesn't cause overfitting.

## Representations: Classes, Trajectories, Transitions
Strong story hypothesis.

Problem parasitic sematics
* combinator
* reification
* localization

We can have representations for objects which can be very vague and general to something more basic to very specific.
For example saying I have a "Tool", we humans cannot imagine or hallucinate anything, because it is very vague.
But if I say I have a hammer, now most of us can imagine something. And if I say A ball and peen hammer, then it becomes even more clear.

But a point to note here is that the information when conveyed from vague to basic level, the ability to imagine something changes drastically. But when we more to more specific the change is not big.

Transition

We tend to think in terms of changes. And we can develop symbols for these representations mostly the vocabulary would contain increase , decrease, change, appear and disappear. For each of these we can have a ! NOT variation. So in total 10 things are possible.



## Quotes
A computer or a person seem intelligent only as long as we don't know how they are solving the problems. The moment the internal working is revealed, the magic is lost and they become dumb again.

## Resources
1. MIT 6.034 Artificial Intelligence, Fall 2010, Instructor: Patrick Winston
