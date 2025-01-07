import random
import time
color = ("Kier", "Trefl", "Serce", "Pik")#Wszystkie kolory w talii
values = {"Dwójka": 2, "Trójka": 3, "Czwórka": 4, "Piątka": 5,"Szóstka": 6, "Siódemka": 7, "Ósemka": 8,
         "Dziewiątka": 9, "Dziesiątka": 10, "Walet": 10, "Dama": 10, "Król": 10, "As": 11}#Wszystkie wartośći kart
ranks = ("Dwójka", "Trójka", "Czwórka", "Piątka", "Szóstka", "Siódemka", "Ósemka", "Dziewiątka", "Dziesiątka",
         "Walet", "Dama", "Król", "As")#Wszstkie rodzaje kart

class karty:#Tworzenie pojedyńczej karty składającej się z koloru oraz nazwy i przypisanej do niej wartości
    def __init__(self,color,rank):
        self.color = color
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " " + self.color

class talia:#Talia składająca się z wszystkich dostępnym kombinacji nazw i kart
    def __init__(self):
        self.talia = []
        for kolor in color:
            for nazwa in ranks:
                created_card = karty(kolor,nazwa)
                self.talia.append(created_card)
    def shuffle(self):#Tasowanie talii
        random.shuffle(self.talia)
    def rozdaj(self):#Rozdanie jednej karty
        return self.talia.pop()

class gracz: #Nazwa gracza oraz jego stan konta
    def __init__(self,nazwa):
        self.nazwa = nazwa
        self.bank = 500
        self.reka = []
    def random(self):#losowanie stanu konta
        self.bank = random.randrange(500,1500,100)
    def wygrana(self,liczba):#dodawanie po wygranej do stanu konta
        self.bank = self.bank + liczba
    def zaklad(self,liczba): #odejmowanie po przegranej do stanu konta
        self.bank = self.bank - liczba
    def dodanie_karty(self,karta): #gracz dobiera karte
        self.reka.append(karta)
    def oddawanie_karty(self): #gracz oddaje wszystkie karty
        self.reka.clear()
    def __str__(self):
        return "Imię: " + self.nazwa + "\nBank: " + str(self.bank) + "$"

class computer:
    def __init__(self):
        self.reka = [] # reka krupiera
    def dodanie_karty(self,karta):
        self.reka.append(karta) # krupier dobiera karte
    def odejmowanie_karty(self):
        self.reka.clear() # krupier konczy dobieranie kart

def start_display():#ekran startowy
    k = 9
    for i in range(0,8):
        k -= 2
        time.sleep(0.5)
        print("* " * i, " " * 10, "* " * (i + k),)
        if k == 1:
            print("* " * 4, "Blackjack ", "* " * 3)
    time.sleep(2)

def zaklad(player):#wydawanie z bankrollu
    while True:
        try:
            time.sleep(0.5)
            zaklad = int(input("Ile chcesz obstawić: "))
            if player.bank < zaklad:
                print("Nie masz tyle pieniędzy!")
                continue
            if zaklad not in range(100,50000,100):
                print("Można stawiać tylko setkami!")
                continue
            else:
                player.zaklad(zaklad)
                return zaklad
        except(ValueError):
            print("Wpisz liczbę!")

def krupier_round(computer,talia,value_gracz):#Runda krupiera
    karta = talia#deck który jest w grze
    gracz_value = value_gracz#wartość gracza
    krupier = computer#obiekt AI
    value_krupier = krupier.reka[0].value + krupier.reka[1].value#Wartość początkowa komputera
    if krupier.reka[0].value == 11 and krupier.reka[1].value == 11:#AS AS
        krupier.reka[1].value = 1
    if krupier.reka[0].value == 11:#AS CHECK
        if value_krupier < 19:
            krupier.reka[0].value = 1
    if krupier.reka[1].value == 11:#AS CHECK
        if value_krupier < 19:
            krupier.reka[1].value = 1
    time.sleep(1)
    print("-" * 15)
    print(f"Krupier: {value_krupier}\nGracz: {gracz_value}")
    print("-" * 15)
    licznik = 1
    while True:
        licznik += 1
        if krupier.reka[0].value + krupier.reka[1].value == 21:#BLACKJACK
            time.sleep(0.5)
            print("Krupier BlackJack!")
            return False
        if gracz_value == "BlackJack":#HAND VS BLACKJACK
            time.sleep(0.5)
            print("Krupier Pass")
            return True
        if value_gracz > 21:#WARUNEK PRZEGRANIA GRACZA
            print("Zbyt dużo kart!")
            return False
        if value_krupier >= gracz_value:#WARUNEK WYGRANIA KRUPIERA
            time.sleep(1)
            print("Krupier wygrywa!")
            return False
        else:
            krupier.dodanie_karty(karta.rozdaj())#DODAWANIE KARTY
            if krupier.reka[licznik].value == 11:#CHECK ACE
                if value_krupier + 1 > 10:
                    krupier.reka[licznik].value = 1
            time.sleep(0.5)
            value_krupier = value_krupier + krupier.reka[licznik].value#DODAWANIE WARTOSCI
            print(f'Krupier dobiera: {krupier.reka[licznik]}\nWartość Krupiera: {value_krupier}')
            if value_krupier > 21:#WARUNEK PRZEGRANIA DOBIERANIA KART
                time.sleep(1)
                print("Krupier Faul!")
                return True

def player_round(player,talia):#Runda gracza
    gracz = player#Obiekt gracza
    karta = talia#Deck który używa gracz
    licznik = 1
    gracz.dodanie_karty(karta.rozdaj()),gracz.dodanie_karty(karta.rozdaj())#Wartość początkowa gracza
    time.sleep(1)
    print(f'Dostałeś: {gracz.reka[0]}, {gracz.reka[1]}')
    if gracz.reka[0].value == 11 and gracz.reka[1].value == 11:  # AS AS
        gracz.reka[1].value = 1
    if gracz.reka[0].value == 11:  # AS
        gracz.reka[0].value = check_ace()
    if gracz.reka[1].value == 11:  # AS
        gracz.reka[1].value = check_ace()
    value = gracz.reka[0].value + gracz.reka[1].value#Wartość początkowa gracza
    while True:
        time.sleep(0.5)
        if gracz.reka[0].value + gracz.reka[1].value == 21:#Blackjack
            time.sleep(0.5)
            print("BlackJack")
            value = "BlackJack"
            return value
        odp = input("Czy chcesz dobrać kolejną karte? ")
        licznik += 1
        if odp.lower() == "tak":
            gracz.dodanie_karty(karta.rozdaj())#Dodawanie kart
            if gracz.reka[licznik].value == 11:#AS CHECK
                if value + 1 > 10:
                    gracz.reka[licznik].value = 1
                else:
                    gracz.reka[licznik].value = check_ace()
            time.sleep(1)
            value = value + gracz.reka[licznik].value#DODAWANIE DO WARTOŚCI
            print(f'Dobrana karta: {gracz.reka[licznik]}\nTwoja wartość: {value}')
            if value > 21:#WARUNEK PRZEGRANIA DOBIERANIA
                time.sleep(0.5)
                return value
            continue
        if odp.lower() == "nie":#ZWRÓCENIE WARTOŚCI
            return value
        else:
            licznik -= 1#LICZNIK NIE NALICZA SIĘ PRZY BŁĘDNIE WPISANYM INPUCIE
            print("Wpisz tak lub nie!")

def check_ace():#Sprawdzanie wartości asa
    while True:
        try:
            odp = int(input("As jako 1 czy As jako 11?: "))
            if odp == 1:
                return 1
            if odp == 11:
                return 11
            else:
                print("Musisz wybrać 1 czy 11!")
                continue
        except(ValueError):
            print("Wpisz liczbę!")
            continue

#Logic Game
start_display()
player = gracz(input("Podaj nazwę użytkownika: "))
krupier = computer()
player.random()
deck = talia()
deck.shuffle()#Tasowanie tali
runda = 0
while runda < 5:
    krupier.odejmowanie_karty()#Czyszczenie rąk
    player.oddawanie_karty()
    if player.bank == 0:#Warunek przegrania gry
        print("Przegrałeś, brak środków na koncie :(")
        break
    print("-" * 12)
    print(player)
    runda += 1
    print("Runda:",runda)
    print("-" * 12)
    pula = zaklad(player)#Zakład któy obstawia gracz
    krupier.dodanie_karty(deck.rozdaj())
    krupier.dodanie_karty(deck.rozdaj())#karty początkowe krupiera
    time.sleep(1)
    print(f'Krupier dostał: {krupier.reka[0]}, Druga karta')
    value_gracz = player_round(player,deck)#wartość gracza wynikająca z rundy gracza
    wynik = krupier_round(krupier, deck, value_gracz)  # Wartość krupiera wynikająca z rundy krupiera
    time.sleep(1.5)
    print("\n" * 10)
    if wynik:  # Jeśli krupier dobierze zbyt dużo kart przegrywa
        player.wygrana(pula * 2)
        print("-" * 15)
        print(f"Wygrałeś: {pula}$")
    if wynik is False:
        print("-" * 15)
        print(f"Przegrałeś {pula}$")
    if runda == 5:  # Koniec gry
        time.sleep(1.5)
        print("\n" * 10)
        if player.bank != 0:
            print(f'Twoja kwota po grze wynosi: {player.bank}$\nGratulacje {player.nazwa}!')
        else:
            print(f"Przykro mi,\nPrzegrałeś twoja pula wynosi {player.bank}$ :(")







































































