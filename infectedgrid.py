#
# The SIR model assumes each infected person is exposed to the total pop with random uniform distribution
# But that's not practically true. An infected person is exposed to a small subset of the total.
# As the infection spreads there will be random subpopulations not reached.
#
# This models the population on a two dimensional grid, like geog space.
# Exposure is simulated using multivariate normal to people proximate to those infected

import numpy as np

# identify the population
# arrange them in a square
population=100
np.arange(population).reshape((int(np.sqrt(population)),int(np.sqrt(population))))
initial = 10
#randomly select initial infections, now infected is a vector of individual index positions
infected = np.random.choice(range(population),initial,replace=False)
# the position of these people is given by
row=np.floor(infected/np.sqrt(100))
col=(infected % np.sqrt(100))

# multivariate normal of contact around an infected person
# rotate this like a diamond
# 0.0049	0.0294	0.0294	0.0049
# 0.0294	0.1764	0.1764	0.0294
# 0.0294	0.1764	0.1764	0.0294
# 0.0049	0.0294	0.0294	0.0049


# randomly select the initial infected over the population grid
infected[0] = 100     # initial population infected
