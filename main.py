import numpy as np

def simulate_secretary_problem(n, k):
    '''
    Simulate the secretary problem with a candidate pool of size n
    k represents the number of candidates to skip before you start considering candidates
    '''
    rankings = np.arange(1, n + 1)
    np.random.shuffle(rankings)

    best_seen = np.min(rankings[:k]) if k > 0 else float('inf')

    acceptable_candidates = rankings[k:] < best_seen
    if np.any(acceptable_candidates):
        # argmax returns the first occurence of the max value, which in this case is 1 because of the boolean array
        return rankings[np.argmax(acceptable_candidates) + k]
    return rankings[-1]


def simulate_rejection(n, k, p=0.5):
    '''
    Simulate the rejection problem with a candidate pool of size n
    k represents the number of candidates to skip before you start considering candidates
    p represents the probability of getting rejected by a candidate
    '''
    rankings = np.arange(1, n + 1)
    np.random.shuffle(rankings)

    best_seen = np.min(rankings[:k]) if k > 0 else float('inf')
    # Setting the ranks of the candidates that reject you to NaN,
    # valid_candidates are those that didn't reject you
    valid_candidates = rankings[k:] * np.where(np.random.rand(n - k) < p, np.nan, 1)

    acceptable_candidates = valid_candidates < best_seen
    if np.any(acceptable_candidates):
        return rankings[np.argmax(acceptable_candidates) + k]
    return rankings[-1]
        

def simulate_going_back(n, k, p=0.5):
    '''
    Simulate the secretary problem with a candidate pool of size n
    In this variation, you can go back to a candidate you've already seen, but may be rejected with probablity p
    If you accept a candiate, you won't be rejected
    k represents the number of candidates to skip before you start considering candidates
    '''
    rankings = np.arange(1, n + 1)
    np.random.shuffle(rankings)

    best_seens = np.sort(rankings[:k])
    best_seen = best_seens[0] if k > 0 else float('inf')
    
    acceptable_candidates = rankings[k:] < best_seen
    if np.any(acceptable_candidates):
        return rankings[np.argmax(acceptable_candidates) + k]
        
    for go_back in range(k):
        # if rejcted, continue to next candidate
        if np.random.random() < p:
            continue
        return best_seens[go_back]

    # Multiply by 1 if not rejected, otherwise make it NaN
    valid_candidates = best_seens * np.where(np.random.rand(k) < p, np.nan, 1)
    return np.min(valid_candidates) # Can do this because we'd be asking the candidates in order
