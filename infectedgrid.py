# identify the population
# arrange them in a square
population=100
np.arange(population).reshape((int(np.sqrt(population)),int(np.sqrt(population))))
# randomly select the initial infected over the population grid
infected[0] = 100     # initial population infected


#https://scaron.info/blog/python-weighted-choice.html
def weighted_choice(seq, weights):
    x = np.random.random()
    for i, elmt in enumerate(seq):
        if x <= weights[i]:
            return elmt
        x -= weights[i]