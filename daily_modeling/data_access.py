from typing import Dict

import pandas as pd
import requests

ENDPOINT = "https://api.thevirustracker.com/free-api?countryTimeline=US"


def get_covid_df(endpoint: str = ENDPOINT) -> pd.DataFrame:
    """ Get JSON data and convert to pandas dataframe

    :param endpoint: string for the covid api url
    :return: pandas dataframe of covid data
    """

    json_data = get_json_data_from_endpoint(endpoint)
    df = covid_df_from_json(json_data)

    return df


def get_json_data_from_endpoint(endpoint: str = ENDPOINT) -> Dict:
    """ Get JSON from the API

    :param endpoint: string for the covid api url
    :return: JSON dictionary
    """

    data = requests.get(endpoint)
    assert data.status_code == 200, "Failure to pull data"

    json_data = data.json()

    return json_data


def covid_df_from_json(json_data: Dict) -> pd.DataFrame:
    """ Convert JSON data from endpoint to pandas dataframe

    :param json_data: JSON dictionary
    :return: dataframe representation
    """

    # get dates from json
    timeline = json_data["timelineitems"][0]
    dates = list(timeline.keys())[:-1]

    # get values for each date
    rows = [{"date": date, **timeline[date]} for date in dates]
    df = pd.DataFrame(rows)
    df.set_index("date", inplace=True)

    return df

