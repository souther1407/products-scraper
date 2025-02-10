from scrapers.fullHard import FullHardScraper
from scrapers.compraGamer import CompraGamerScraper
from config import config
from requester.seleniumRequester import SeleniumRequest


class App:
    def __init__(self):
        self.scrapers = [FullHardScraper(), CompraGamerScraper(),]

    def start(self):
        for s in self.scrapers:
            s.scrape()


if __name__ == "__main__":
    app = App()
    app.start()
    # full_hard = FullHardScraper()
    # full_hard.scrape()
    # compra_gamer = CompraGamerScraper()
    # compra_gamer.scrape()
