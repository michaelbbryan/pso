# total population
POPULATION: int = 326000000

# how many days is an infected person sick thru recovery
DURATION: int = 14

# how many people does an infected person contact per day
CONTACTS: int = 12

# if exposed, the prob a susceptible contact will get infected
INFECTION_RATE: float = .017857

# Coronavirus has an R0 of 3 people, so duration x contacts x rate = 3
# at the end of the sickness what proportion recovers
RECOVERY_RATE: float = .97

# number of days to view the process
PERIOD: int = 180

# how many people are initially sick
INITIAL_INFECTIONS: int = 10
