pula = int(input("Wpisz pule: "))
bet = int(input("Wpisz bet: "))
out = int(input("Wpisz ilość outów: "))
pot_odds = (bet/pula) * 100
hand_equality = out * 2
if hand_equality > pot_odds:
    print("Pot Oddsy: ",pot_odds,"%")
    print("Equlity: ",hand_equality,"%")
    print("Equlity River: ", hand_equality / 2, "%")
    print("Equality +")
else:
    print("Pot Oddsy: ", pot_odds, "%")
    print("Equlity: ", hand_equality, "%")
    print("Equlity River: ", hand_equality/2, "%")
    print("Equality -")


