import configparser
import json

config = configparser.ConfigParser()
config.read('config.ini')
with open('products.json', 'r', encoding='UTF-8') as json_file:
    products = json.load(json_file)