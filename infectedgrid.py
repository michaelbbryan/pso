"""
    The SIR model assumes each infected person is exposed to the total pop with random uniform distribution
    But that's not practically true. An infected person is exposed to a small subset of the total.
    As the infection spreads there will be random subpopulations not reached.

    This models the population on a two dimensional grid, like geog space.
    Exposure is simulated using multivariate normal to people proximate to those infected
"""

import numpy as np
import pandas as pd
import random
from default_values import POPULATION, DURATION, PERIOD, INITIAL_INFECTIONS, RECOVERY_RATE

random.seed(1234)

POPULATION = 1000000
assert np.sqrt(POPULATION).is_integer()

# Initialize the city as a list of people
#      each person starts Infected=False, Susceptibe=True
infected = np.full((POPULATION), False, dtype=bool)
infected_duration = np.full((POPULATION), 0, dtype=int)
susceptible = np.full((POPULATION), True, dtype=bool)

# Initialize the simulation results
results = pd.DataFrame(columns = ['Day' , 'Infected', 'Died' , 'Recoverd'])

# Randomly distribute the initial infections
for p in np.random.choice(range(POPULATION),initial,replace=False):
    infected[p] = True


for day in range(PERIOD): # iterate over time
    # first recover or die off those infected for the DURATION
    for i in range(POPULATION):
        if infected_duration[i] = 14:
            infected_duration = 0
            susceptible[i] = False

    rows.append({"Day": day, "Died": died, "Recovered": recovered, "Infected": infected[0]})

    RECOVERY_RATE

    for each proximate
        for offsetx in range(-2,,3,1):
            for offsety in range(-2,,3,1):
                if susceptible[x+offsetx,y+offsety]
        infect only those susceptible
        applying the distributed probabilities


        # the position of these people is given by
        row = np.floor(infected / np.sqrt(100))
        col = (infected % np.sqrt(100))


        # multivariate normal of contact around an infected person
        # 0.005	    0.005	0.005	    0.005	0.005
        # 0.005	    0.08	0.15	    0.08	0.005
        # 0.005	    0.15	infected	0.15	0.005
        # 0.005	    0.08	0.15	    0.08	0.005
        # 0.005	    0.005	0.005   	0.005	0.005

        results = results.append({"Day": day,
                                  "Died": died,
                                  "Recovered": recovered,
                                  "Infected": sum(infected)},
                                 ignore_index = True)
