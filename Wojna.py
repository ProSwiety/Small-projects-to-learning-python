import random
values = {'Two': 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
          "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
class Card:
    def __init__(self,suit,rank):
        self.suit = suit#kolor karty
        self.rank = rank#wartość karty
        self.value = values[rank]#Wartość karty w systemie
    def __str__(self):
        return self.rank + " of " +self.suit# np Two of Hearts

class Deck:
    def __init__(self):
        self.all_cards = []
        # Create the Card object
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards) # po utworzeniu talii kart losowo tasuje talie
    def deal_one(self):
        return self.all_cards.pop() # rozdaje karte graczowi i usuwa ją z talii
class Player:
    def __init__(self,name):
        self.name = name # imie gracza
        self.all_cards = [] # talia gracza

    def remove_one(self):
        return self.all_cards.pop(0) #gracz zagrywa karte
    def add_cards(self,new_cards):
     #Dołączanie wielu kart w formie listy
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards) #.extend dołącza do danej listy wiele obiektów
    #Dołączanie pojedyńczej karty
        else:
            self.all_cards.append(new_cards)



    def __str__(self):
        return f'Player{self.name} has {len(self.all_cards)} cards.'






