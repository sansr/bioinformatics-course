#! /usr/bin/python3

def composition(genome, k):
    """Generates all reads of length k in genome (alphabetical order)"""
    return sorted([text[i:i+k] for i in range(len(text)-k+1)])


def string_from_genome_path(reads):
    """Reconstructs a genome from its genome path composed by all the reads generated"""
    k = len(reads[0])
    sequence = reads[0]
    for read in reads[1:]:
        sequence = sequence + read[k-1:] 
    return sequence

def overlap_graph(reads):
    """Computed the overlap graph in which nodes are the reads and the edges represent the overlaping relation between nodes."""
    check_overlap = lambda pair: pair[0][1:] == pair[1][:-1]

    pairs = ((read1, read2) for i, read1 in enumerate(reads) for j, read2 in enumerate(reads) if i != j)
    graph = filter(check_overlap, pairs)
    return graph

def deBruijin_graph(k, sequence):
    """Compute the de Bruijing graph from a sequence and a k given. In the de Bruijin graph the edges represente the reads and the nodes are overlaps between this reads"""
    graph = {}
    edges = list([sequence[i:i+k] for i in range(len(sequence)-k+1)])
    for edge in edges:
        frm = edge[:-1]
        to = edge[1:]
        if frm in graph:
            graph[frm].append(to)
        else:
            graph[frm] = [to]

    return graph

def deBruijin_graph_from_edges(edges):
    """Compute the de Bruijing graph from a number os edges given. In the de Bruijin graph the edges represent the reads and the nodes are overlapsbetween this reads"""
    graph = {}
    for edge in edges:
        frm = edge[:-1]
        to = edge[1:]
        if frm in graph:
            graph[frm].append(to)
        else:
            graph[frm] = [to]

    return graph

        
if __name__ == "__main__":
    import sys

    with open(sys.argv[1], 'r') as f:
        #lines = f.read().splitlines()

        ### Composition test ###
        # k = int(lines[0])
        # text = lines[1]
        # result = composition(text, k)

        # for kmer in result:
        #     print(kmer)

        ### String spelled test ###
        #print(string_from_genome_path(lines))

        ### Overlaps ###
        #graph = overlap_graph(lines)

        # for pair_nodes in graph:
        #     print (pair[0] + ' -> ' + pair[1])

        ### De Bruijin graph generated from a sequence ###
        # k = int(f.readline())
        # sequence = f.readline().rstrip()
        # graph = deBruijin_graph(k, sequence)
        
        # for k, v in sorted(graph.items()):
        #     print(k + ' -> ' + ','.join(v))
        

        ### De Bruijin graph generated from the isolated edges that ###
        ### represent the reads                                     ###
        sequence = f.read().splitlines()
        graph = deBruijin_graph_from_edges(sequence)
        
        for k, v in sorted(graph.items()):
            print(k + ' -> ' + ','.join(v))
