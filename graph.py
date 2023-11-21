import matplotlib.pyplot as plt
import numpy as np

def graph(outcomes, optimal_k, probablity=None, theoretical_optimal_k=False, savefig=False, filename='graph.png'):
    plt.figure(figsize=(16, 9))
    
    plt.rcParams["font.family"] = "Cascadia Mono"
    # change background color
    plt.rcParams['axes.facecolor'] = '#040227'
    # change the entire screen color
    plt.rcParams['figure.facecolor'] = '#040227'
    plt.rcParams['savefig.facecolor'] = '#040227'


    # change color of axis lines
    plt.rcParams['axes.edgecolor'] = '#FFFFFF'
    # change color of tick labels
    plt.rcParams['ytick.color'] = '#FFFFFF'
    plt.rcParams['xtick.color'] = '#FFFFFF'
    # change color of axes labels
    plt.rcParams['axes.labelcolor'] = '#FFFFFF'
    # change color of figure title
    plt.rcParams['figure.titlesize'] = 20
    plt.rcParams['figure.titleweight'] = 'bold'
    # change color of axes title
    plt.rcParams['axes.titlesize'] = 16
    plt.rcParams['axes.titleweight'] = 'bold'
    plt.rcParams['axes.titlecolor'] = '#FFFFFF'

    plt.rcParams['axes.titlesize'] = 24
    
    # make lines a little bit thicker
    plt.rcParams['lines.linewidth'] = 5

    # remove top and right borders
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)


    plt.plot(outcomes, color='#df3b43')
    
    # draw vertical lines
    plt.axvline(x=optimal_k, color='#21cda2', linestyle='--')

    if theoretical_optimal_k:
        theoretical_optimal_k = len(outcomes) / np.e
        plt.axvline(x=theoretical_optimal_k, color='#3673d6', linestyle=':')

    # draw horizontal line at the maximum
    plt.axhline(y=np.max(outcomes), color='#3673d6', linestyle='--')
    
    plt.xlabel('Looking to Leaping Threshold', size=20, labelpad=25)
    if not probablity:
        plt.ylabel('Probability of Choosing Best Apartment', size=20, labelpad=25)
        plt.title(f'Finding the Best of {len(outcomes)} Apartments', size=35)
    else:
        plt.ylabel('Probability of Finding the Best Partner', size=20, labelpad=25)
        plt.title(f'Finding the Best Partner with {int(probablity * 100)}% Chance of Rejection', size=30)

    plt.legend(['Probability', f'Optimal k ({optimal_k})', f"Maximum Probablity ({np.max(outcomes)})"], labelcolor='#FFFFFF', fontsize=20) #f'Probability Optimal k ({int(np.round(theoretical_optimal_k, 0))})'
    
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)

    # make xticks integers
    if len(outcomes) < 11:
        plt.xticks(np.arange(0, len(outcomes), 1.0))


    if savefig:
        plt.savefig(filename, dpi=600, bbox_inches='tight')
    else:
        plt.show()
