from config import env
import requests


class ApiService:
    def storeProducts(self, products):
        response = requests.post("http://localhost:8080/products", json={"products": products},
                                 headers={"Content-type": "Application/json"})
