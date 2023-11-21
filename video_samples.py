import numpy as np
import random

def simulate_secretary_problem_from_video(n, k):
    '''
    Simulate the secretary problem with a candidate pool of size n
    k represents the number of candidates to skip before you start considering candidates
    '''
    ranking = np.arange(1, n + 1)
    np.random.shuffle(ranking)

    best_seen = float('inf')
    for look in range(k):
        if ranking[look] < best_seen:
            best_seen = ranking[look]
    # best_seen = np.min(ranking[:k]) if k > 0 else float('inf')

    for leap in range(k, n):
        if ranking[leap] < best_seen:
            return ranking[leap]
    return ranking[-1]

def simulate_rejection_from_video(n, k, p=0.5):
    rankings = list(range(1, n + 1))
    random.shuffle(rankings)

    # Look phase
    best_seen = float('inf')
    for look in range(k):
        if rankings[look] < best_seen:
            best_seen = rankings[look]

    # Leap phase, but with rejection
    for leap in range(k, n):
        if rankings[leap] < best_seen:
            # if rejected, continue to next candidate
            if np.random.random() < p:
                continue
            return rankings[leap]
    return rankings[-1]

def simulate_going_back_from_video(n, k, p=0.5):
    rankings = list(range(1, n + 1))
    random.shuffle(rankings)

    # Look phase
    best_seen = float('inf')
    for look in range(k):
        if rankings[look] < best_seen:
            best_seen = rankings[look]
    
    # Leap phase
    for leap in range(k, n):
        if rankings[leap] < best_seen:
            return rankings[leap]
    
    # Go back phase
    best_seens = sorted(rankings[:k])
    for go_back in range(k):
        # if rejcted, continue to next candidate
        if np.random.random() < p:
            continue
        return best_seens[go_back]

    return best_seens[-1]