from loader import config, products
from random import choice, choices, randint

class Cash:
    def __init__(self, number):
        self.number = number
        self.cheque = []
        
    def generate_cheque_for_day(self):
        for _ in range(randint(int(config['cash']['min_number_cheque_per_day']),
                               int(config['cash']['max_number_cheque_per_day']))):
            self.generate_cheque()
        return self.cheque
            
        
    def generate_cheque(self):
        number_items = randint(int(config['cash']['min_products_in_cheque']),
                               int(config['cash']['max_products_in_cheque']))
        doc_id = self.__generate_doc_id()
        for _ in range(number_items):
            category = self.__generate_category()
            item, price = self.__generate_item_and_price(category)
            amount = self.__generate_amount()
            discount = self.__generate_discount()
            self.cheque.append((doc_id, item, category, amount, price, discount))
    
    def __generate_doc_id(self):
        doc_id = []
        cheque_symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        for _ in range(int(config['cash']['len_cheque_id'])):
            doc_id.append(choice(cheque_symbols))
        return ''.join(doc_id)
    
    def __generate_category(self):
        return choice(list(products.keys()))
    
    def __generate_item_and_price(self, category):
        product = choice(products[category])
        return product['название'], product['цена']
    
    def __generate_amount(self):
        return randint(1, 5)
    
    def __generate_discount(self):
        return choices([0, 10, 15], weights=[0.8, 0.15, 0.05], k=1)[0]  # чем больше скидка, тем реже она выпадает
    
    