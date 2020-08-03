import requests


class Request:
    def __init__(self):
        # url to ask randomuser.me API for same set of persons like in attached persons.json file.
        self.url = 'https://randomuser.me/api/?seed=abc&page=1&results=1000&version=1.3'

        self.response = requests.request("GET", self.url)

    def from_api(self):
        return self.response.json().get('results')





