from requester.seleniumRequester import SeleniumRequest
from config import config
from bs4 import BeautifulSoup
from services.api import ApiService


class CompraGamerScraper:
    def __init__(self):
        self.storeName = "Compra gamer"
        self.urlBase = "https://compragamer.com"
        self.routesCategories = config["tiendas"]["compragamer"]
        self.requester = SeleniumRequest()
        self.api = ApiService()

    def getProducts(self, html, category):
        products = []
        soup = BeautifulSoup(html, "html.parser")
        productsContainer = soup.find(
            "div", attrs={"class": "addRow ng-star-inserted"})
        for p in productsContainer.find_all("cgw-product-alone"):
            imgLink = p.find("img")["src"]
            price = p.find("h1", attrs={"class": "price"}).find("span").text
            link = self.urlBase + p.find("a")["href"]
            name = p.find("div", attrs={"class": "theme_nombreProducto"}).find(
                "span").text
            products.append(
                {"categoria": category, "nombre": name, "precio": price, "link": link, "img": imgLink, "tienda": self.storeName})

        return products

    def scrape(self):
        products = []
        for category in self.routesCategories:
            print(f"scrapeando en categoria {category}")
            for subcategoryRoute in self.routesCategories[category]:
                html = self.requester.request(
                    self.urlBase + subcategoryRoute)
                newProducts = self.getProducts(html, category)
                products += newProducts
                self.api.storeProducts(newProducts)

        print(f"total productos: {len(products)}")
