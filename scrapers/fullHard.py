from requester.plainRequester import PlainRequester
from bs4 import BeautifulSoup
from config import config
import json


class FullHardScraper:
    def __init__(self):
        self.storeName = "fullhard"
        self.urlBase = "https://fullh4rd.com.ar"
        self.routesCategories = config["tiendas"]["fullhard"]
        self.requester = PlainRequester()

    def getProducts(self, html, category):
        soup = BeautifulSoup(html, "html.parser")
        products = []
        productsContainer = soup.find("div", id="gallery-list")
        for p in productsContainer.find_all("div", attrs={"class": "item product-list"}):
            product = {"nombre": p.h3.text, "url": self.urlBase +
                       p.a["href"], "img": self.urlBase + p.img["src"], "precio": p.find("div", attrs={"class": "price"}).text.split(" ")[0], "tienda": self.storeName, "categoria": category}
            products.append(product)
        return products

    def scrape(self):
        currentPage = 1
        products = []
        for routeCategory in self.routesCategories:
            print(f"scraping en sección {routeCategory}")
            for subCategory in self.routesCategories[routeCategory]:
                currentPage = 1
                print(f"scraping en url {subCategory}")
                while (True):
                    print(f"pag: {currentPage}")
                    html = self.requester.request(
                        self.urlBase + subCategory + str(currentPage))
                    currentPageProducts = self.getProducts(html, routeCategory)
                    if (len(currentPageProducts) == 0):
                        break
                    products += currentPageProducts
                    currentPage += 1
        print(f"total productos encontrados: {len(products)}")
        with open("output.json", "w+", encoding="utf8") as file:
            file.write(json.dumps(products))
        return products
