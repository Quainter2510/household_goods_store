from loader import config
from shop import Shop

if __name__ == '__main__':
    shops = []
    for i in range(int(config['shop']['count_shops'])):
        shop = Shop(i)
        shop.upload_cashes()