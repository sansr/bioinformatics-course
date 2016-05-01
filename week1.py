import sys

def PatternCount(Pattern, Genome):
    """Returns the number of times a pattern appears in Genome"""
    count = 0
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == pattern:
            count += 1
    return count

def CountDict(Genome, k):
    """Returns a dictionary in which associates the index of
    each k-mer (pattern of length k) with the number of ocurrences"""
    Count = {}
    for i in range(len(Genome)-k+1):
        Pattern = Genome[i:i+k]
        Count[i] = PatternCount(Pattern, Genome)
    return Count

def FrequentWords(Genome, k):
    """Returns most frequent k-mer in Genome"""
    FrequentPatterns = []
    Count = CountDict(Genome, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Genome[i:i+k])
    return list(set(FrequentPatterns))

def ReverseComplement(Genome):
    """Computes the Genome's reverse complement"""
    complements = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    rText = reversed(Genome)
    rcomplement = ''
    for n in rText:
        rcomplement += complements[n]
    return rcomplement

def PatternMatching(Pattern, Genome):
    """Calculates the positions where Pattern appears in Genome"""
    indices = list()
    offset = 0
    i = Genome.find(Pattern, offset)
    while i >= 0:
        indices.append(str(i))
        i = Genome.find(Pattern, i+1)
    return indices
