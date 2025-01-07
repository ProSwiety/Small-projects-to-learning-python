import time
import random
a = [3, 2, 1]
wc = 0
wg = 0
W = "Wygrałeś!"
P = "Przegrałeś :("
A = "Dziękujemy za grę"
J = "Witamy w grze Orzeł czy Reszka"
lista1 = []
print("-" * len(J))
print(J)
print("-" * len(J))
time.sleep(1)
print("Za 3 sekundy rozpocznie się gra!")
time.sleep(3)
print("Start!")
while True:
    k = random.choice(["orzeł", "reszka"])
    for s in a:
        time.sleep(1)
        print(s)
    time.sleep(1)
    print("Start!")
    u = input("Orzeł czy Reszka? ")
    if u.lower() != "orzeł" and u.lower() != "reszka":
        print("Podano złą odpowiedź!")
        continue
    time.sleep(1)
    print("Komputer wybrał: :", k)
    if u.lower() != k.lower():
        lista1.append(u.lower())
        wc += 1
        print("Pudło!, Wynik komputera to: ", wc)
        if wc >= 5:
            break
    elif u.lower() == k.lower():
        lista1.append(u.lower())
        wg += 1
        print("Trafiłeś!, Twój wynik to: ", wg)
        if wg >= 5:
            break
if wc > wg:
    print("*" * len(P))
    print(P)
    print("*" * len(P))
elif wg > wc:
    print("*" * len(W))
    print(W)
    print("*" * len(W))
    Tak = "tak" or "nie"
    while Tak != "nie" or Tak != "tak":
        Tak = input("Czy chcesz zapisać do tablicy? ")
        if Tak.lower() == "tak":
            plik = open("../Projekty i inne/test.txt", "a")
            n = (input("Podaj nazwę użytkownika: "))
            plik.write(str(n + " " + str(wg) + " " + str(wc) + "\n"))
            plik = open("../Projekty i inne/test.txt")
            tablica = (plik.read())
            print(tablica)
            plik.close()
            print("*" * len(A))
            print(A)
            print("*" * len(A))
            break
        elif Tak == "nie":
            print("*" * len(A))
            print(A)
            print("*" * len(A))
            break
        else:
            print("Błędna odpowiedź!")
            continue
n = 6
while n > 5 or n <= 0 or n == str:
    try:
        n = int(input("Oceń aplikację w skali 1-5: "))
        if n <= 5 and n > 0:
            plik = open("../Projekty i inne/ocena.txt", "a")
            plik.write(str(n))
            plik.close()
            plik = open("../Projekty i inne/ocena.txt", "r")
            lista = []
            for l in plik.readline():
                lista.append(int(l))
            plik.close()
            print("-" * 40)
            print("Liczba Ocen:",len(lista))
            print("Średnia ocena aplikacji:",round(sum(lista) / len(lista), 2),"/ 5")
            break
        else:
            print("Podaj prawidłową wartość!")
    except:
        print("Nie wpisałeś cyfry!")
print("Ilość wybranych orłów:", lista1.count("orzeł"))
print("Ilość wybranych reszek:", lista1.count("reszka"))
v = wc + wg
w = ((wg / v) * 100)
print("Twoja procentowa ilość trafień:",round((w), 1),"%")
print("-" * 40)