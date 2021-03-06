# graph-random-connection-simulations
Initial statement of problem from Joshua Zelinsky:

There is an idea in mathematics of a "graph," not in the sense you may have heard of y=f(x), but rather in the sense of a network with a collection of special points, which are called vertices or nodes, which are connected if they share some relation. For example, on a social network like Facebook, one might imagine that each person is a node and two nodes are connected if they are friends. We say a graph is connected if one can travel along edges from any given node to any other node. For example, consider the friend graph of Alice, Bob, Carol, Diane and Eric, it might be that Alice, is friends with Bob who is friends with Carol, and Diane is friends with Eric. This graph is not connected since there's no way to get from Eric to Alice. But if Bob became friends with Diane, then this graph would now be connected.

Here is a question I don't know the answer to. Suppose that we make a graph using the following process. We start with n points, and no edges. For our first step, we pick a random node (Which for convenience we'll call 1). We then pick a second random node, we'll call 2 and add an edge between those two nodes. We then move to our new node 2, which we just connected. We now pick a random node which does not have an edge connected to 2, connect that one, call it 3, and then move to 3, continuing this process. We'll stop when the entire graph is connected. On average, for a given n, about how long do we expect it to take before the graph is connected? This isn't immediately obvious, since in our process, by bad luck we can go back to a previous node which is already connected. For example, from node 3, we might end up going back to node 1, which is essentially a wasted move.

Here's a related question: We say a subset of nodes of a graph is a clique if every element in that set has an edge connecting to every other element.  In terms of friends this means that every person in the group is friends with every other person in that group of people. For example, consider the friend graph of Alice, Bob, Carol, Diane, Eric, and Fred. Suppose that Alice, Bob and Carol is each friends with the other two.  Carol is also friends with Diane who is friends with Eric who is friends with Fred.  And there are no other friend relations. Then we have a clique of size 3 from Alice, Bob and Carol, and no larger clique exists in the graph

In our above process of making a graph by randomly adding edges, for a given n, what do we expect on average the largest clique to  be in the graph we have formed?

# Using the code
- Run `pipenv install` to install the dependencies
- Run `pipenv run python run-simulations.py` to run simulations and write results to results.tsv
- Run `pipenv run python analyse.py` to generate a summary table of the results by node count and graphs showing average steps and average maximal clique size by node count

# Configuration
You can change how many simulations to run and what node sizes to test by editing the global variables at the top of run-simulations.py
