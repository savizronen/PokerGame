import random
class Card:
  def __init__(self,card_number,suit_symbol):
    self.suit_symbol = suit_symbol
    self.card_number = card_number
    self.texture=self.card_view()



  def card_view(self):
    """Display all the cards in the cards list."""
    rows = ['', '', '', '', '', '']  # The text to display on each row.

    # The card's front:
    rank, suit = self.card_number,self.suit_symbol  # The card is a tuple data structure.
    rows[0] += '.-----.'
    rows[1] += '|{}    |'.format(rank)
    rows[2] += '|  {}  |'.format(suit)
    rows[3] += '|    {}|'.format(rank)
    rows[4] += '`-----´'

    return rows


