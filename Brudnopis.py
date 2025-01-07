from random import randint
a = randint(1,9)
b = 0
while True:
    b += 1
    user = input("Wpisz liczbe: ")
    if user == "exit":
        break
    elif int(user) > a:
        print("Too high")
    elif int(user) < a:
        print("Too low")
    else:
        print(f'Gratulację! zgadłeś za {b} razem')
        break
