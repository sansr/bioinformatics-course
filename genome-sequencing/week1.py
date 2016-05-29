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

if __name__ == "__main__":
    import sys

    with open(sys.argv[1], 'r') as f:
        lines = f.read().splitlines()

        # Composition test
        # k = int(lines[0])
        # text = lines[1]
        # result = composition(text, k)

        # for kmer in result:
        #     print(kmer)

        # String spelled test
        print(string_from_genome_path(lines))
