import requests
from bs4 import BeautifulSoup
from scrapers.fullHard import FullHardScraper

class App:
    def __init__(self):
        self.scrapers = []


if __name__ == "__main__":
    app = App()
    fullHard=FullHardScraper()
    fullHard.scrape()
    
