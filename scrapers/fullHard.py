from requester.plainRequester import PlainRequester

class FullHardScraper:
    def __init__(self,url):
        self.url = url
        self.requester = PlainRequester()

    def scrape(self):
        pass