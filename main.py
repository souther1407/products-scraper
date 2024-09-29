import requests

class App:
    def __init__(self):
        self.scrapers = []



if __name__ == "__main__":
    app = App()
    response = requests.get(url="https://google.com")
    print(response.text)
