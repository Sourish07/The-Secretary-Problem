import numpy as np
import matplotlib.pyplot as plt

apartments = [1, 2, 3] # 1 is the best apartment, 3 is the worst

NUM_OF_SIMULATIONS = 1000
chosen_apartments = []

for _ in range(NUM_OF_SIMULATIONS):
    # Shuffling because we don't the know the order in which we'll see the apartments
    np.random.shuffle(apartments)
    
    FIRST_APT = apartments[0]
    SECOND_APT = apartments[1]
    THIRD_APT = apartments[2]

    if SECOND_APT < FIRST_APT:
        chosen_apartments.append(SECOND_APT)
    else:
        chosen_apartments.append(THIRD_APT)

plt.figure(figsize=(16, 9))

plt.rcParams["font.family"] = "Cascadia Mono"
# change background color
plt.rcParams['axes.facecolor'] = '#040227'
# change the entire screen color
plt.rcParams['figure.facecolor'] = '#040227'

# change color of axis lines
plt.rcParams['axes.edgecolor'] = '#FFFFFF'
# change color of tick labels
plt.rcParams['ytick.color'] = '#FFFFFF'
plt.rcParams['xtick.color'] = '#FFFFFF'
# change color of axes labels
plt.rcParams['axes.labelcolor'] = '#FFFFFF'
# change color of axes title
plt.rcParams['axes.titlesize'] = 50
plt.rcParams['axes.labelsize'] = 50
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.titlecolor'] = '#FFFFFF'

# remove top and right borders
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)


n, bins, patches = plt.hist(chosen_apartments, bins=[0.5, 1.5, 2.5, 3.5], align='mid', rwidth=0.8, color=['#df3b43'])
plt.xticks([1, 2, 3], ["Best", "Middle", "Worst"], fontsize=30)

# Customizing the y-axis to show proportions
counts, _ = np.histogram(chosen_apartments, bins=3)
total_count = np.sum(counts)
proportions = counts / total_count
plt.yticks(ticks=counts, labels=[f"{p:.2f}" for p in proportions], fontsize=30)

plt.title("Choosing the Best of Three Apartments", pad = 25)
plt.xlabel("Chosen Apartment", labelpad = 25)
plt.ylabel("Proportion", labelpad = 25)

plt.savefig("three_bar_chart.png", dpi=600, bbox_inches='tight', facecolor=plt.rcParams['figure.facecolor'])