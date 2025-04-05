from loader import config
from shop import Shop
from datetime import datetime

if __name__ == '__main__':
    if datetime.now().date().weekday() != 6:
        shops = []
        for i in range(int(config['shop']['count_shops'])):
            shop = Shop(i)
            shop.upload_cashes()