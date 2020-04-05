from data_access import get_covid_df


def weighted_exponential():

    # get data from default covid endpoint
    df = get_covid_df()

    new_deaths = df["new_daily_deaths"]
    new_deaths = new_deaths[new_deaths > 100]
    new_deaths = new_deaths.to_frame()

    new_deaths["new_daily_deaths_shifted"] = new_deaths["new_daily_deaths"]
    new_deaths["new_daily_deaths_shifted"] = new_deaths["new_daily_deaths_shifted"].shift()
    new_deaths = new_deaths.iloc[1:]

    new_deaths["ratio"] = new_deaths["new_daily_deaths"] / new_deaths["new_daily_deaths_shifted"]
    new_deaths["smoothed_ratio"] = new_deaths["ratio"].ewm(halflife=1).mean()


if __name__ == "__main__":
    weighted_exponential()