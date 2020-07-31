import requests


class Request:
    def __init__(self):
        self.url = 'https://randomuser.me/api/?seed=abc&page=1&results=1000&version=1.3'
        self.response = requests.request("GET", self.url)

    def from_api(self):
        return self.response.json()


R = Request()
for x in R.from_api().get('results'):
    print(x)
    print("\n")
