import numpy as np
import matplotlib.pyplot as plt


N = 1501
NUM_SIMULATIONS = 1000

def hi(p, threshold):
    # p = proportion of parking spots taken
    # threshold = number of spots away from the destination
    # Destination is at the middle of the road: 75th spot

    road = np.random.random(N) < p # True means occupied, False means empty

    for i in range(threshold, N):
        if not road[i]:
            return i
    return N

    
def hi2(p):
    D = int(N / 2)
    avg_dists = []
    best_avg_dist = None
    for i in range(D + 1):
        avg_dist = 0
        for _ in range(NUM_SIMULATIONS):
            parking_spot = hi(p, i)
            distance_to_destination = abs(parking_spot - D)

            avg_dist += distance_to_destination
        avg_dist /= NUM_SIMULATIONS
        avg_dists.append(avg_dist)

        if best_avg_dist is None or avg_dist < best_avg_dist:
            best_avg_dist = avg_dist
            best_i = abs(i - D)

    print(best_i, best_avg_dist)
    plt.plot(avg_dists)
    plt.show()

hi2(0.9999)
