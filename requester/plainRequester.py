import requests

class PlainRequester:
    def request(self,url):
        respose = requests.get(url)
        return respose.text