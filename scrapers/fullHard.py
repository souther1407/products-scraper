from requester.plainRequester import PlainRequester
from bs4 import BeautifulSoup
class FullHardScraper:
    def __init__(self):
        self.urlBase = "https://fullh4rd.com.ar"
        self.routesCategories = ["/cat/185/discos-ssd/"]
        self.requester = PlainRequester()

    def getProducts(self,html):
        soup = BeautifulSoup(html,"html.parser")
        products = []
        productsContainer = soup.find("div",id="gallery-list")
        for p in productsContainer.find_all("div",attrs={"class":"item product-list"}):
            product={"nombre": p.h3.text,"url":self.urlBase + p.a["href"],"img":self.urlBase + p.img["src"],"precio":p.find("div",attrs={"class":"price"}).text.split(" ")[0]}
            products.append(product)
        return products


    def scrape(self):
        currentPage = 1
        thereIsProducts = True
        products = []
        for routeCategory in self.routesCategories:
            while(thereIsProducts):
                print(f"pag: {currentPage}")
                html = self.requester.request(self.urlBase + routeCategory + str(currentPage))
                currentPageProducts = self.getProducts(html)
                if(len(currentPageProducts) == 0):
                    thereIsProducts = False
                    continue
                products += currentPageProducts
                currentPage += 1

        print(f"total productos encontrados: {len(products)}")    