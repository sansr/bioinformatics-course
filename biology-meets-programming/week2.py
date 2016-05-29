## Module with functions implemented for week2 exercises of the course ##

from week1 import PatternCount
import sys

def SymbolArray(genome, symbol):
    """Returns the number of  symbol occurrences in genome"""
    counts = {}
    n = len(genome)
    ExtendedGenome = genome + genome[0:n//2]
    for i in range(n):
        counts[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])

    return counts

def FasterSymbolArray(genome, symbol):
    """Faster version of the SymbolArray function"""
    array = {}
    n = len(genome)
    ExtendedGenome = genome + genome[0:n//2]
    array[0] = PatternCount(symbol, genome[0:n//2])
    for i in range(1, n):
        array[i] = array[i-1]
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1

    return array

def Skew(genome):
    """Calculates the C and G fluctuations in genome. Goal: find the point in which the reverse half-strand ends and the forwards half-strand begins"""
    skew = {0: 0}
    for i in range(len(genome)):
        if genome[i] == 'G':
            skew[i+1] = skew[i]+1
        elif genome[i] == 'C':
            skew[i+1] = skew[i]-1
        else:
            skew[i+1] = skew[i]

    return skew

def MinSkew(genome):
    """Find the positions where the skew diagram reaches a minimun"""
    skew = Skew(genome)
    min_value = min(skew.values())
    return [k for k in skew if skew[k] == min_value]

def HammingDistance(p, q):
    """Auxiliary function that computes the hamming distance between two items"""
    mismatches = 0
    for item1, item2 in zip(p,q):
        if item1 != item2:
            mismatches += 1
            
    return mismatches

def ApproximatePatternMatching(pattern, genome, d):
    """Find all approximate ocurrences of a pattern in genome with at most d mismatches"""
    positions = list()
    for i in range(len(genome)-len(pattern)+1):
        ptt = genome[i:i+len(pattern)]
        if HammingDistance(pattern, ptt) <= d:
            positions.append(i)

    return positions    

def ApproximatePatternCount(pattern, genome, d):
    """Computes the number of occurrences of patter in genome with at most d mmismatches"""
    count = 0
    for i in range(len(text)-len(pattern)+1):
        ptt = text[i:i+len(pattern)]
        if HammingDistance(pattern, ptt) <= d:
            count += 1

    return count
