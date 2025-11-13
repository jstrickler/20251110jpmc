class Card:  # inherits from class 'object'
    def __init__(self, rank, suit):
        self._rank = rank
        self.suit = suit

    @property # decorator
    def rank(self):  # replace function 'rank' with decorator 'rank'
        return self._rank
    
    @rank.setter
    def rank(self, value):
        if isinstance(value, str):
            self._rank = value
        else:
            raise TypeError(f"rank must be str, not {type(value).__name__}")

    @property
    def suit(self):
        return self._suit
    
    @suit.setter
    def suit(self, value):
        if isinstance(value, str):
            self._suit = value
        else:
            raise TypeError(f"suit must be str, not {type(value).__name__}")
    

    def __str__(self):
        return f"Card:{self.rank}/{self.suit}"

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"


if __name__ == "__main__":
    c1 = Card("8", "Diamonds")
    print(f"{type(c1) = }")
    
    print(c1)  # uses str()
    print(f"{c1 = }")  # uses repr()
    print(repr(c1))
    print(f"{c1.rank = }")
    print(f"{c1.suit = }")
    c1.rank = '2'
    # c1.rank = 123
