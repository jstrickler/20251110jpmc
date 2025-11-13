import random
from card import Card

class CardDeck:
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self):
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()
    
    def __len__(self):
        return len(self._cards)
    
    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}()"
    
    def __str__(self):
        class_name = type(self).__name__
        return f"{class_name}:{len(self)}"

if __name__ == "__main__":
    d1 = CardDeck()
    print(f"{d1 = }")
    d1.shuffle()
    print(d1.cards)
    # d1.shuffle()
    for _ in range(8):
        card = d1.draw()
        print(f"{card = }")
    print(f"{len(d1) = }")
    print(d1)
