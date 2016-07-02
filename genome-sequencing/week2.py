from week1 import deBruijn_graph_from_edges
from itertools import product

def cycle(edges, current_node):
    path = [current_node]

    while True:
        path.append(edges[current_node][0])

        if len(edges[current_node]) > 1:
            edges[current_node] = edges[current_node][1:]
        else:
            del edges[current_node]

        if path[-1] in edges:
            current_node = path[-1]
        else:
            break
    return (path, edges)
    

def EulerianCycle(edges):
    """Generates a Eulerian cycle from given edges"""
    current_node = edges.keys()[0]
    (path, edges) = cycle(edges, current_node)

    while len(edges) > 0:
        for i in range(len(path)):
            if path[i] in edges:
                current_node = path[i]
                (expansion_cycle, edges) = cycle(edges, current_node)
                path = path[:i] + expansion_cycle + path[i+1:]

    return path

def EulerianPath(edges):
    path = []
    # Calculates the ooutdegree and indegree value for each node
    indegree = {}
    for values in edges.values():
        for value in values:
            if value in indegree:
                indegree[value] += 1
            else:
                indegree[value] = 1

    outdegree = {edge:len(edges[edge]) for edge in edges}

    for k in outdegree.keys():
        if k not in indegree:
            indegree[k] = 0
    
    for k in indegree.keys():
        if k not in outdegree:
            outdegree[k] = 0
        if indegree[k] < outdegree[k]:
            node_to = k
        elif indegree[k] > outdegree[k]:
            node_from = k

    # Add the edge needed to have a balanced graph
    if node_from in edges:
        edges[node_from].append(node_to)
    else:
        edges[node_from] = [node_to]

    # Computes the Eulerian cycle
    cycle = EulerianCycle(edges)
    
    # Get the point in the cycle in which the previous edge to
    # get a balanced graph has been introduced
    unbalanced_point = filter(lambda i: cycle[i:i+2] == [node_from, node_to], range(len(cycle)-1))[0]
    
    return cycle[unbalanced_point+1:]+cycle[1:unbalanced_point+1]

def string_reconstruction(k, reads):
    graph = deBruijn_graph_from_edges(reads)

    with open('salida.txt', 'w') as output:
        for k, v in sorted(graph.items()):
            output.write(k + ' -> ' + ','.join(v) + '\n')

    with open('salida.txt', 'r') as input_file:
        lins = input_file.read().splitlines()
        edges = {}
        for edge in [line.split(" -> ") for line in lins]:
            if ',' in edge[1]:
                edges[edge[0]] = map(str, edge[1].split(','))
            else:
                edges[edge[0]] = [str(edge[1])]

        final_path = EulerianPath(edges)
        result = [final_path[0]] + map(lambda s: s[-1], final_path[1:])

        return result

def universal_string(k):
    universal_dict = {}
    for kmer in [''.join(item) for item in product('01', repeat=k)]:
        if kmer[:-1] in universal_dict:
            universal_dict[kmer[:-1]].append(kmer[1:])
        else:
            universal_dict[kmer[:-1]] = [kmer[1:]]

    path = EulerianCycle(universal_dict)
    return ''.join([item[0] for item in path[:-1]])

if __name__ == "__main__":
    import sys

    with open(sys.argv[1], 'r') as f:
        lines = f.read().splitlines()

        ### Eulerian Cycle ###

        # Build edges from input
        # edges = {}
        # for edge in [line.split(" -> ") for line in lines]:
        #     if ',' in edge[1]:
        #         edges[int(edge[0])] = map(int, edge[1].split(','))
        #     else:
        #         edges[int(edge[0])] = [int(edge[1])]
            
            
        # EulerCycle = map(str, EulerianCycle(edges))
        # print('->'.join(EulerCycle))

        ### Eulerian path ###

        # Build edges from input
        # edges = {}
        # for edge in [line.split(" -> ") for line in lines]:
        #     if ',' in edge[1]:
        #         edges[int(edge[0])] = map(int, edge[1].split(','))
        #     else:
        #         edges[int(edge[0])] = [int(edge[1])]

        # #EulerianPath(edges)
        # EulerPath = map(str, EulerianPath(edges))
        # print('->'.join(EulerPath))

        ### String reconstruction problem ###
        # k = int(lines[0])
        # reads = lines[1:]
        # assembled = string_reconstruction(k, reads)
        # print "".join(assembled)

        ### Universal string problem ###
        k = int(lines[0])
        print(universal_string(k))

            
