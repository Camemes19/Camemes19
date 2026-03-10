import requests
from requests import RequestException


def fetch_mal_data(config):
    headers = {"X-MAL-CLIENT-ID": config.clientId,}
    try:
        response = requests.get(f"{config.baseUrl}users/DrDewm/animelist?sort=list_score&status"
                                "=completed&limit=10",
                                headers=headers)
        if response.status_code == requests.codes.OK:
            return response.json()["data"]
    except ConnectionError as err:
        print(f"Error occurred during API Call: {err}")

fetch_mal_data()