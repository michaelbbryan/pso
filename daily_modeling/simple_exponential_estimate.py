import fire

from data_access import get_covid_df


def predicted_number_dead(n_days: int, smoothed_exp_halflife: int = 7) -> int:
    """

    :param n_days:
    :param smoothed_exp_halflife:
    :return:
    """

    # get data from default covid endpoint
    df = get_covid_df()

    new_deaths = df["new_daily_deaths"]
    new_deaths = new_deaths[new_deaths > 100]
    new_deaths = new_deaths.to_frame()

    new_deaths["new_daily_deaths_shifted"] = new_deaths["new_daily_deaths"]
    new_deaths["new_daily_deaths_shifted"] = new_deaths["new_daily_deaths_shifted"].shift()
    new_deaths = new_deaths.iloc[1:]

    new_deaths["ratio"] = new_deaths["new_daily_deaths"] / new_deaths["new_daily_deaths_shifted"]
    new_deaths["smoothed_ratio"] = new_deaths["ratio"].ewm(halflife=7).mean()

    last_day_death_count = df["new_daily_deaths"].iloc[-1]
    smoothed_exponent = new_deaths["smoothed_ratio"].iloc[-1]

    total_dead = df["total_deaths"].iloc[-1]
    forecasted_deaths = [int(round(last_day_death_count * (smoothed_exponent ** day)))
                         for day in range(1, n_days+1)]

    print(f"Forecasted deaths per day: {forecasted_deaths}")

    return total_dead + sum(forecasted_deaths)


if __name__ == "__main__":

    fire.Fire(predicted_number_dead)