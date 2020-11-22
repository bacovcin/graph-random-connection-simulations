import numpy as np
import matplotlib.pyplot as plt


def main():
    results = {}
    with open('results.tsv') as infile:
        infile.readline()
        for line in infile:
            sline = line.rstrip().split('\t')
            try:
                results[sline[0]]['steps'].append(int(sline[2]))
                results[sline[0]]['clique_size'].append(int(sline[3]))
            except KeyError:
                results[sline[0]] = {}
                results[sline[0]]['steps'] = [int(sline[2])]
                results[sline[0]]['clique_size'] = [int(sline[3])]
    with open('summary.txt', 'w') as outfile:
        outfile.write('node_count\tmin_steps\tmean_steps\tmedian_steps\tmax_steps\tmin_clique_size\tmean_clique_size\tmedian_clique_size\tmax_clique_size\n')
        counts = []
        stepAvgs = []
        cliqueAvgs = []
        for nodeCount in results:
            counts.append(nodeCount)
            steps = np.array(results[nodeCount]['steps'])
            clique_size = np.array(results[nodeCount]['clique_size'])
            stepAvgs.append(steps.mean())
            cliqueAvgs.append(clique_size.mean())
            outfile.write(f'{nodeCount}\t{steps.min()}\t{steps.mean()}\t{np.median(steps)}\t{steps.max()}\t{clique_size.min()}\t{clique_size.mean()}\t{np.median(clique_size)}\t{clique_size.max()}\n')
        plt.plot(counts, stepAvgs, label='Average steps by node count')
        plt.xlabel('Node counts')
        plt.ylabel('Avg number of steps to full connectivity')
        plt.savefig('steps.pdf')
        plt.close()
        plt.plot(counts, cliqueAvgs, label='Average steps by node count')
        plt.xlabel('Node counts')
        plt.ylabel('Avg size of maximal clique at full connectivity')
        plt.savefig('cliques.pdf')
        plt.close()


if __name__ == '__main__':
    main()
