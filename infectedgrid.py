"""
    The SIR model assumes each infected person is exposed to the total pop with random uniform distribution
    But that's not practically true. An infected person is exposed to a small subset of the total.
    As the infection spreads there will be random subpopulations not reached.

    This models the population on a two dimensional grid, like geog space.
    Exposure is simulated using multivariate normal to people proximate to those infected
"""
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import random
from default_values import POPULATION, DURATION, PERIOD, INITIAL_INFECTIONS, RECOVERY_RATE
import matplotlib.animation as an

random.seed(1234)
POPULATION = 10000
assert np.sqrt(POPULATION).is_integer()  # the population should be a square

# If an infected person has two layers of proximate contacts
# a multivariate normal grid around that person looks like
PROXIMATE_PROB = np.array([[0.005, 0.005, 0.005, 0.005, 0.005], \
                           [0.005, 0.080, 0.150, 0.080, 0.005], \
                           [0.005, 0.150,     0, 0.150, 0.005], \
                           [0.005, 0.080, 0.150, 0.080, 0.005], \
                           [0.005, 0.005, 0.005, 0.005, 0.005]])

# Dampen prox probability to 14 day expected value of 3 infections
for x in range(5):
    for y in range(5):
        PROXIMATE_PROB[x,y] = (3/14) * PROXIMATE_PROB[x,y]

# Initialize the city as a list of people
#      each person starts Infected=False, Susceptibe=True
infected = np.full((POPULATION), False, dtype=bool)
infected_duration = np.zeros((POPULATION),dtype=int)
susceptible = np.full((POPULATION), True, dtype=bool)

# Initialize the simulation results
results = pd.DataFrame(columns = ['Day' , 'Infected', 'Died' , 'Recovered', 'Susceptible'])

# Randomly distribute the initial infections
initial = np.random.choice(range(POPULATION),INITIAL_INFECTIONS,replace=False)
for p in initial:
    infected[p] = True
    susceptible[p] = False

susceptible_history = {}

for day in range(180): # iterate over time
    print("day",day,"infected",sum(infected))
    # first recover or die off those who have been infected for the DURATION
    died = 0
    recovered = 0
    for i in range(POPULATION):
        if infected_duration[i] == DURATION:
            infected_duration[i] = 0
            infected[i] = False
            susceptible[i] = False
            if np.random.choice([True, False], 1, p=[RECOVERY_RATE, 1-RECOVERY_RATE]):
                recovered += 1
            else:
                died += 1
    # next spread the disease from each infected person
    for i in range(POPULATION):
        if infected[i]:
            # project the disease onto the proximate square
            for y in range(PROXIMATE_PROB.shape[0]):
                for x in range(PROXIMATE_PROB.shape[1]):
                    square = int((i + (y - 2) * np.sqrt(POPULATION)) + (x - 2))
                    if square >= 0 and square < POPULATION:
                        if susceptible[square]:
                            if np.random.choice([True, False], 1, p=[PROXIMATE_PROB[x,y], 1 - PROXIMATE_PROB[x,y]]):
                                susceptible[square] = False
                                infected[square] = True
    # increase the time of those infected
    for i in range(POPULATION):
        if infected[i]:
            infected_duration[i] += 1
    # store the day's results
    results = results.append({"Day": day,
                              "Died": died,
                              "Recovered": recovered,
                              "Infected": sum(infected),
                              "Susceptible": sum(susceptible)},
                                 ignore_index = True)
    # and record the infection history
    susceptible_history[day] = susceptible

def infection_trend(r):
    fig = plt.figure()
    ax = plt.axes()
    ax.plot(r['Day'], r['Infected'])
    plt.text(160,2,(POPULATION-sum(susceptible)))
    plt.show()


def frame_function(d):
    #animation function for the heat function below, update the heatmap object
    heatmap = s[d].astype(int).reshape(int(np.sqrt(POPULATION)), int(np.sqrt(POPULATION)))
    im.set_array(heatmap)
    return [im]

def heat(s):
    fps = 30
    nSeconds = 6
    fig = plt.figure( figsize=(int(np.sqrt(POPULATION)),int(np.sqrt(POPULATION))) )
    heatmap = s[0].astype(int).reshape(int(np.sqrt(POPULATION)),int(np.sqrt(POPULATION)))
    im = plt.imshow(heatmap, cmap='hot', interpolation='nearest')
    anim = an.FuncAnimation(
                               fig,
                               frame_function,
                               frames = fps * nSeconds,
                               interval = 60000 / fps, # in ms
                               )
    plt.show()
    #anim.save('test_anim.mp4', fps=fps, extra_args=['-vcodec', 'libx264'])
    return()

heat(susceptible_history)