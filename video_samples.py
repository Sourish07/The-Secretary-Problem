import random
import matplotlib.pyplot as plt


def simulate_secretary_problem(n, k):
    # Generating apartments and shuffling
    rankings = list(range(1, n + 1))
    random.shuffle(rankings)
    
    # Look phase, reject all and keep track of best
    best_seen = float('inf')
    for look in range(k):
        if rankings[look] < best_seen:
            best_seen = rankings[look]
    
    # Leap phase, choose the first that beats the best seen so far
    for leap in range(k, n):
        if rankings[leap] < best_seen:
            return rankings[leap]
        
    return rankings[-1]


def simulate_rejection(n, k, p=0.5):
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
            if random.random() < p:
                continue
            return rankings[leap]
    return rankings[-1]


def simulate_going_back(n, k, p=0.5):
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
    # Go to the best candidate you saw in the look phase
    # If rejected, move onto the second best, etc.
    best_seens = sorted(rankings[:k])
    for go_back in range(k):
        if random.random() < p:
            continue
        return best_seens[go_back]

    return best_seens[-1]


if __name__ == "__main__":
    CANDIDATE_POOL_SIZE = 100 # (n)
    NUM_SIMULATIONS = 1000

    outcomes = []
    for ltl_threshold in range(CANDIDATE_POOL_SIZE): # look then leap threshold (k)
        best_apt_count = 0
        for _ in range(NUM_SIMULATIONS):
            chosen_apt = simulate_going_back(CANDIDATE_POOL_SIZE, ltl_threshold)
            if chosen_apt == 1:
                best_apt_count += 1
        outcomes.append(best_apt_count / NUM_SIMULATIONS)

    plt.plot(outcomes)
    plt.show()