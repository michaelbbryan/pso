import fire

from data_access import get_covid_df


def predicted_number_dead(n_days: int, smoothed_exp_halflife: int = 7) -> int:
    """ Predict the number of dead n_days in the futre

    :param n_days: number of days in the future
    :param smoothed_exp_halflife: number of days to smooth over
    :return: the total number of predicted dead
    """

    # get data from default covid endpoint
    df = get_covid_df()

    # filter for new daily deaths (only looking after daily counts exceeded 100)
    # TODO: maybe remove this restriction
    new_deaths = df["new_daily_deaths"]
    new_deaths = new_deaths[new_deaths > 100]
    new_deaths = new_deaths.to_frame()

    # get a column that is shifted forward a day
    new_deaths["new_daily_deaths_shifted"] = new_deaths["new_daily_deaths"]
    new_deaths["new_daily_deaths_shifted"] = new_deaths["new_daily_deaths_shifted"].shift()
    new_deaths = new_deaths.iloc[1:]

    # calculate the ratio of one day to the day before
    new_deaths["ratio"] = new_deaths["new_daily_deaths"] / new_deaths["new_daily_deaths_shifted"]

    # smooth over time to improve stability
    new_deaths["smoothed_ratio"] = new_deaths["ratio"].ewm(halflife=smoothed_exp_halflife,
                                                           ignore_na=True).mean()

    # get the most recent number of daily deaths
    last_day_death_count = df["new_daily_deaths"].iloc[-1]

    # get the smoothed exponent for projection forward
    smoothed_exponent = new_deaths["smoothed_ratio"].iloc[-1]

    # get the total number of deaths
    total_dead = df["total_deaths"].iloc[-1]

    # project deaths per day
    forecasted_deaths = [int(round(last_day_death_count * (smoothed_exponent ** day)))
                         for day in range(1, n_days+1)]

    print(f"Forecasted deaths per day: {forecasted_deaths}")

    # sum of the deaths each day
    return total_dead + sum(forecasted_deaths)


if __name__ == "__main__":
    fire.Fire(predicted_number_dead)
