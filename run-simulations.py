from random import choice

import networkx as nx

MIN_NUM_OF_NODES = 5        # Smallest number of nodes to simulate
MAX_NUM_OF_NODES = 100       # Maximum number of nodes to simulate
STEPS_NUM_OF_NODES = 1      # Number of nodes to jump starting at the minimum
NUM_OF_SIMULATIONS = 100    # Number of simulations to run for each node number


def create_graph(nodeNum):
    g = nx.Graph()
    for i in range(nodeNum):
        g.add_node(i)
    return g, set(g.nodes)


def main():
    with open('results.tsv', 'w') as outfile:
        outfile.write('node_count\tsimulation_num\tnum_of_steps\tmax_clique_size\n')
        for n in range(MIN_NUM_OF_NODES, MAX_NUM_OF_NODES, STEPS_NUM_OF_NODES):
            print(f'Running simulations for node number: {n}')
            for i in range(NUM_OF_SIMULATIONS):
                g, nodeSet = create_graph(n)
                startNode = choice(tuple(nodeSet))
                steps = 0
                while not nx.is_connected(g):
                    choices = tuple(nodeSet - set([startNode] + list(nx.neighbors(g, startNode))))
                    newNode = choice(choices)
                    g.add_edge(startNode, newNode)
                    startNode = newNode
                    steps += 1
                outfile.write(f'{n}\t{i}\t{steps}\t{max([len(x) for x in nx.find_cliques(g)])}\n')


if __name__ == '__main__':
    main()
