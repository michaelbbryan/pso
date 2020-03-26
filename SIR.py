import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from default_values import POPULATION, DURATION, CONTACTS, INFECTION_RATE, \
    RECOVERY_RATE, PERIOD


def simulate_infection(population: int = POPULATION, duration: int = DURATION,
                       contacts: int = CONTACTS, infection_rate: float = INFECTION_RATE,
                       recovery_rate: float = RECOVERY_RATE,
                       period: int = PERIOD, verbose: bool = True) -> pd.DataFrame:
    """ Simple SIR simulation

    :param population: total population
    :param duration: how many days an infected person is sick through recover
    :param contacts: how many people does an infected person contact per day
    :param infection_rate: if exposed, the prob a susceptible contact will get infected
    :param recovery_rate: at the end of the sickness what proportion recovers
    :param period: number of days to view the process
    :param verbose: boolean for print control
    :return: pandas dataframe with day, number dead, recovered, and infected
    """

    # initialize the initial number of infected individuals
    infected = np.zeros(duration)
    infected[0] = 100

    # initialize number recovered, dead, and dataframe rows
    recovered, died, rows = 0, 0, []

    for day in range(period):

        # recover or die off those who have been infected for the duration
        recovered = recovered + recovery_rate * infected[duration - 1]
        died = died + (1 - recovery_rate) * infected[duration - 1]

        # roll all values one position to the right, set the first value to the last
        infected = np.roll(infected, shift=1)
        infected[0] = infected[-1]

        # infect a new generation
        susceptible = np.maximum(population - np.sum(infected) - died - recovered, 0)
        infected[0] = np.around(np.sum(infected) * infection_rate * contacts * (susceptible / population))

        # add to dataframe
        rows.append({"Day": day, "Died": died, "Recovered": recovered, "Infected": infected[0]})

    df = pd.DataFrame(rows)

    if verbose:
        pd.options.display.float_format = '{:,.0f}'.format
        print(df.to_string())

    return df


def plot_occurences(df: pd.DataFrame) -> None:
    """ Plot summary line graph

    :param df: dataframe
    """

    sns.lineplot(data=df, x="Day", y="Infected")
    plt.show()


if __name__ == "__main__":

    df = simulate_infection()
    plot_occurences(df)
