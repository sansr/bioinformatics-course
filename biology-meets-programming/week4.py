## Module with functions implemented for week4 exercises of the course ##

def count_with_pseudocounts(motifs):
    columns = [''.join(seq) for seq in zip(*motifs)]
    return [[c.count(nucleotide)+1 for c in columns] for nucleotide in 'ACGT']

def compute_col_det(motifs):
    dets = []
    columns = [''.join(seq) for seq in zip(*motifs)]
    for nucleotide in 'ACGT':
        det = 0
        for c in columns:
            det += c.count(nucleotide)
        dets.append(det)

    return dets
            
def profile_with_pseudocounts(motifs):
    matrix = count_with_pseudocounts(motifs)
    nrows = len(motifs)+4
    return [[col/nrows for col in row] for i, row in enumerate(matrix)]

def greedy_motif_search_pseudocounts(dna, k, t):
    bestMotifs = []
    # Add the first kmer as the best motif
    for i in range(t):
        bestMotifs.append(dna[i][0:k])

    for i in range(len(dna[0])-k+1):
        motifs = [dna[0][i:i+k]]
        for j in range(1, t):
            p = profile_with_pseudocounts(motifs[0:j])
            motifs.append(profile_most_probable_pattern(dna[j], k, p))
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs

    return bestMotifs

def Motifs(profile, dna):
    motifs = []
    k = len(profile[0])
    for row in dna:
        motifs.append(profile_most_probable_pattern(row, k, profile))

    return motifs

def random_motifs(dna, k, t):
    rMotifs = []
    for row in range(0,t):
        rn = random.randint(1, len(dna[row]))
        rMotifs.append(dna[row][rn:rn+k])

    return rMotifs

def randomized_motif_search(dna, k, t):
    bestMotifs = random_motifs(dna, k, t)
    while True:
        profile = profile_with_pseudocounts(bestMotifs)
        motifs = Motifs(profile, dna)
        print(motifs)
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs
        else:
            return bestMotifs

## Gibbs sampling ##

def normalize(probabilities):
    sum = 0
    for k,v in probabilities.items():
        sum += v
    
    return {k:v/sum for k,v in probabilities.items()}


def weighted_die(probabilities):
    kmer = '' # output variable
    meres = []

    for k,v in probabilities.items():
        meres.append((k, v))
    intervalos = []

    for i in range(len(meres)):
        intervalos.append((intervalos[i-1] if i > 0 else 0)+meres[i][1])
        
    rand = random.uniform(0, 1)
    
    for i in range(len(intervalos)):
        if rand <= intervalos[i]:
            kmer = meres[i][0]
            break
    
    return kmer
    
def profile_generated_string(text, profile, k):
    probabilities = {}
    for i in range(len(text)-k+1):
        probabilities[text[i:i+k]] = pr(text[i:i+k], profile)
        
    probabilities = normalize(probabilities)
    return weighted_die(probabilities)

