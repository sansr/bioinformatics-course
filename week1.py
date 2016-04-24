import sys

def PatternCount(pattern, text):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        Count[i] = PatternCount(Pattern, Text)
    return Count

def FrequentWords(Text, k):
    FrequentPatterns = []
    Count = CountDict(Text, k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    return list(set(FrequentPatterns))

def ReverseComplement(Text):
    complements = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    rText = reversed(Text)
    rcomplement = ''
    for n in rText:
        rcomplement += complements[n]
    return rcomplement

def PatternMatching(pattern, genome):
    indices = set()
    offset = 0
    i = genome.find(pattern, offset)
    while i >= 0:
        indices.add(str(i))
        i = genome.find(pattern, i+1)
    return indices
