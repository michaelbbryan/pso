#
# Attempt to simulate an epidemic using SIR modelling
# Initial pass uses 1 population, later to have multi community spread with origin/destination flows
#


import numpy as np
import matplotlib.pyplot as plt

population = 326000000

duration = 14          # how many days is an infected person sick thru recovery
contacts = 12          # how many people does an infected person contact per day
infection_rate = .017857   # if exposed, the prob a susceptible contact will get infected
                       # Coronavirus has an R0 of 3 people, so duration x contacts x rate = 3
recovery_rate = .97    # at the end of the sickness what proportion recovers
period: int = 180      # number of days to view the process

infected = np.zeros(duration)
infected[0] = 100     # initial population infected
recovered = 0
died = 0

days=[i for i in range(0,period)]    # vector of days
cases=np.zeros(period)               # vector of infections including the initial

for t in range(period):
    # recover or die off those who have been infected for the duration
    recovered = recovered + recovery_rate * infected[duration - 1]
    died = died + (1 - recovery_rate) * infected[duration - 1]
    # age the infected population
    for d in range(duration):
        infected[duration - d - 1] = infected[duration - d - 2]
    # infect a new generation
    susceptible = np.maximum(population - np.sum(infected) - died - recovered,0)
    infected[0] = np.around(np.sum(infected) * infection_rate * contacts * (susceptible / population))
    cases[t]=infected[0]  # update the case tracking vector
    print("Time\t", t,
          "\tdied\t",
          "{0:,.0f}".format(died),
          "\trecovered\t", "{0:,.0f}".format(recovered),
          "\tinfected\t", "{0:,.0f}".format(infected[0]))

plt.style.use('seaborn-colorblind')
plt.plot(days, cases)
plt.show()

# S,I,R concepts:
#     A closed community of susceptible people, gets an infected person
#     A person who is infected for a duration then either recovers or dies
#     While the person is infected they have a number of contacts:
#         a subset is susceptible (original population minus those already infected, recovered or dead)
#         of the susceptible contacts some proportion get infected
#     So the infection spreads, iterating over time, quickly at first since many are susceptible
#         then slower as their are fewer susceptible until the virus dies because it cant find a new host

# Interaction between communities:
#     metropolitan statistical areas (MSAs)
#     consolidated metropolitan statistical areas (CMSAs)
#     primary metropolitan statistical areas (PMSAs)
