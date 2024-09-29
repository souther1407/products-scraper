import requests

class PlainRequester:
    def request(url):
        respose = requests.get(url)
        return respose.text