from loader import config
from cash import Cash
import csv 
import os

class Shop:
    def __init__(self, numder):
        self.numder = numder
        self.cashes = []
        for i in range(int(config['shop']['count_cashs'])):
            self.cashes.append(Cash(i))
    
    def upload_cashes(self):
        for i in range(int(config['shop']['count_cashs'])):
            cheque = self.cashes[i].generate_cheque_for_day()
            self.create_csv(cheque, self.cashes[i].number)
            
    def create_csv(self, cheque, cash_number):
        curr_dir = os.path.dirname(__file__)
        with open(os.path.join(curr_dir, 'data', f'{self.numder}_{cash_number}.csv'), 'w', encoding='UTF-8') as file:
            writter = csv.writer(file, delimiter=';')
            writter.writerow(('doc_id', 'item', 'category', 'amount', 'price', 'discount'))
            writter.writerows(cheque)