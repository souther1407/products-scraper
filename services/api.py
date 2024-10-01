from config import env
import requests


class ApiService:
    def storeProducts(self, products):
        requests.post(env.API_URL, json=products)
