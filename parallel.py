import numpy as np
from main import simulate_secretary_problem, simulate_rejection, simulate_going_back
from graph import graph
from multiprocessing import Pool
import os

CANDIDATE_POOL_SIZE = 100
NUM_SIMULATIONS = 20_000
NUM_OF_PROCESSES = os.cpu_count()
CHOSEN_FUNCTION = simulate_secretary_problem

def run_simulation(k):
    counter = 0
    for _ in range(NUM_SIMULATIONS):
        chosen_candidate = CHOSEN_FUNCTION(CANDIDATE_POOL_SIZE, k)
        if chosen_candidate == 1: # 1 is the best candidate
            counter += 1
    return counter


if __name__ == "__main__":
    with Pool(np.min([NUM_OF_PROCESSES, CANDIDATE_POOL_SIZE])) as p:
        results = p.map(run_simulation, range(CANDIDATE_POOL_SIZE))
    outcomes = [count / NUM_SIMULATIONS for count in results]
    optimal_k = np.argmax(outcomes)

    graph(outcomes, optimal_k, savefig=True)
