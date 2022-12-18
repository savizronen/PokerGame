import random
from  card import Card
class Cards:

    def __init__(self):
        self.user_cards=[]
        self.computer_cards = []


    def add_user_card(self,card_number,suit_symbol):

        self.user_cards.append(Card(card_number,suit_symbol))

    def add_computer_card(self, card_number, suit_symbol):
        self.computer_cards.append(Card(card_number, suit_symbol))