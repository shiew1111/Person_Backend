import requests
from requests import ConnectionError


def get_people_from_api():
    # url to ask randomuser.me API for same set of persons like in attached persons.json file.
    url = 'https://randomuser.me/api/?seed=abc&page=1&results=1000&version=1.3'
    try:
        response = requests.request("GET", url)

        return response.json().get('results')
    except ConnectionError:
        print("No connection to API")
