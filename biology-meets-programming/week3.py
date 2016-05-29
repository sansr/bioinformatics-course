## Module with functions implemented for week3 exercises of the course ##

import random
from collections import defaultdict

def count(motifs):
    """Calculates the number of ocurrences of each nucleotide"""
    columns = [''.join(seq) for seq in zip(*motifs)]
    return [[c.count(nucleotide) for c in columns] for nucleotide in 'ACGT']

def profile(motifs):
    """Generates a profile matrix according to some motifs given"""
    matrix = count(motifs)
    nrows = len(motifs)
    return [[col/nrows for col in row] for row in matrix]

def score(motifs):
    """Returns the score of the given list of motifs."""
    columns = [''.join(seq) for seq in zip(*motifs)]
    max_count = sum([max([c.count(nucleotide) for nucleotide in 'ACGT']) for c in columns])

    return len(motifs[0])*len(motifs) - max_count

def pr(text, profile):
    """Returns the probability that text happens according to profile matrix"""
    nuc_loc = {'A':0, 'C':1, 'G':2, 'T':3}
    p = 1
    
    for j, nucleotide in enumerate(text):
	    p *= profile[j][nuc_loc[nucleotide]]

    return p

def consensus(motifs):
    countM = count(motifs)
    k_mer = len(motifs[0])
    consensus = ""

    for j in range(k_mer):
        m = 0
        frequentSymbol = ""
        for k,v in countM.items():
            if v[j] > m:
                m = v[j]
                frequentSymbol = k
        consensus += frequentSymbol
    
    return consensus

def profile_most_probable_pattern(text, k, profile):
    """Returns the most probable pattern according to a profile matrix"""
    max_prob = [-1, None]
    
    for i in range(len(text)-k+1):
        prob = pr(text[i:i+k], profile)
        if prob > max_prob[0]:
            max_prob = [prob, text[i:i+k]]

    return max_prob[1]

def greedy_motif_search(dna, k, t):
    """Searches the best motifs using a greedy algorithm"""
    bestMotifs = []
    # Add the first kmer as the best motif
    for i in range(t):
        bestMotifs.append(dna[i][0:k])

    for i in range(len(dna[0])-k+1):
        motifs = [dna[0][i:i+k]]
        for j in range(1, t):
            p = profile(motifs[0:j])
            motifs.append(profile_most_probable_pattern(dna[j], k, p))
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs

    return bestMotifs

