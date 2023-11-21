import numpy as np
import matplotlib.pyplot as plt

def simulate_secretary_problem_from_video(n, k):
    '''
    Simulate the secretary problem with a candidate pool of size n
    k represents the number of candidates to skip before you start considering candidates
    '''
    ranking = np.arange(1, n + 1)
    np.random.shuffle(ranking)

    best_seen = np.min(ranking[:k]) if k > 0 else float('inf')

    for leap in range(k, n):
        if ranking[leap] < best_seen:
            return ranking[leap]
    return ranking[-1]


def simulate_rejection(n, k, p=0.5):
    '''
    Simulate the rejection problem with a candidate pool of size n
    k represents the number of candidates to skip before you start considering candidates
    p represents the probability of getting rejected by a candidate
    '''
    ranking = np.arange(1, n + 1)
    np.random.shuffle(ranking)

    best_seen = np.min(ranking[:k]) if k > 0 else float('inf')

    for leap in range(k, n):
        if ranking[leap] < best_seen:
            # if rejected, continue to next candidate
            if np.random.random() < p:
                continue
            return ranking[leap]
    return ranking[-1]


def simulate_going_back(n, k, p=0.5):
    '''
    Simulate the secretary problem with a candidate pool of size n
    In this variation, you can go back to a candidate you've already seen, but may be rejected with probablity p
    If you accept a candiate, you won't be rejected
    k represents the number of candidates to skip before you start considering candidates
    '''
    rankings = np.arange(1, n + 1)
    np.random.shuffle(rankings)

    best_seens = sorted(rankings[:k])
    best_seen = best_seens[0] if k > 0 else float('inf')
    
    for leap in range(k, n):
        if rankings[leap] < best_seen:
            return rankings[leap]
        
    for go_back in range(k):
        # if rejcted, continue to next candidate
        if np.random.random() < p:
            continue
        return best_seens[go_back]

    return best_seens[-1]


if __name__ == "__main__":
    CANDIDATE_POOL_SIZE = 100
    NUM_SIMULATIONS = 1000

    outcomes = []
    for ltl_threshold in range(CANDIDATE_POOL_SIZE): # look then leap threshold
        best_apt_count = 0
        for _ in range(NUM_SIMULATIONS):
            chosen_apt = simulate_going_back(CANDIDATE_POOL_SIZE, ltl_threshold)
            if chosen_apt == 1:
                best_apt_count += 1
        outcomes.append(best_apt_count / NUM_SIMULATIONS)

    plt.plot(outcomes)
    plt.show()
