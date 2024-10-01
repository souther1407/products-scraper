from scrapers.fullHard import FullHardScraper
from config import config
from requester.seleniumRequester import SeleniumRequest
from services.api import ApiService


class App:
    def __init__(self):
        self.scrapers = [FullHardScraper()]
        self.apiService = ApiService()

    def start(self):
        products = []
        for s in self.scrapers:
            products += s.scrape()
        self.apiService.storeProducts(products)


if __name__ == "__main__":
    app = App()
    # fullHard = FullHardScraper()
    # fullHard.scrape()
