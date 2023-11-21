import numpy as np
from main import simulate_secretary_problem, simulate_rejection, simulate_going_back
from graph import graph
from multiprocessing import Pool

CANDIDATE_POOL_SIZE = 100
NUM_OF_PROCESSES = 20
NUM_SIMULATIONS = 10_000

# PROBABLITY = 0.5

def run_simulation(k):
    counter = 0
    for _ in range(NUM_SIMULATIONS):
        chosen_candidate = simulate_going_back(CANDIDATE_POOL_SIZE, k)
        if chosen_candidate == 1:
            counter += 1
    return counter


if __name__ == "__main__":
    with Pool(np.min([NUM_OF_PROCESSES, CANDIDATE_POOL_SIZE])) as p:
        results = p.map(run_simulation, range(CANDIDATE_POOL_SIZE))
    outcomes = [count / NUM_SIMULATIONS for count in results]
    optimal_k = np.argmax(outcomes)

    graph(outcomes, optimal_k, savefig=True, filename=f"output.png")
