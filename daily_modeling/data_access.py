from typing import Dict

import pandas as pd
import requests

ENDPOINT = "https://api.thevirustracker.com/free-api?countryTimeline=US"


def get_covid_df(endpoint: str = ENDPOINT) -> pd:
    """

    :param endpoint:
    :return:
    """

    json_data = get_json_data_from_endpoint(endpoint)
    df = covid_df_from_json(json_data)

    return df


def get_json_data_from_endpoint(endpoint: str = ENDPOINT) -> Dict:
    """

    :param endpoint:
    :return:
    """

    data = requests.get(endpoint)
    assert data.status_code == 200, "Failure to pull data"

    json_data = data.json()

    return json_data


def covid_df_from_json(json_data: Dict) -> pd.DataFrame:
    """

    :param json_data:
    :return:
    """

    timeline = json_data["timelineitems"][0]
    dates = list(timeline.keys())[:-1]

    rows = [{"date": date, **timeline[date]} for date in dates]
    df = pd.DataFrame(rows)
    df.set_index("date", inplace=True)

    return df

