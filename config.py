import json
from dotenv import load_dotenv
import os
load_dotenv()

env = {
    "API_URL":os.getenv("API_URL")
}
config={}

with open("./config.json","r",encoding="utf8") as file:
    fileStr = file.read()
    config = json.loads(fileStr)