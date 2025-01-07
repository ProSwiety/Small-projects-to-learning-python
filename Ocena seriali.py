def skrpyt_imiona():
    M = ["Paweł", "Patryk", "Fabian"]
    K = ["Paulina", "Ania", "Kasia"]
    x = input("Podaj imię: ")
    if x == M[0] or x == M[1] or x == M[2]:
        print("Imię męskie")
        print("Koniec")
    elif x == K[0] or x == K[1] or x == K[2]:
        print("Imię żeńskie")
        print("Koniec")
    else:
        print("Nie znaleziono imienia")
        if True:
            tak = input("Czy chcesz dodać? ")
            if tak == "tak":
                imie = x
                x = input("Czy jest to imię męskie?")
            if x == "tak":
                M.append(imie)
                print("Imię męskie", (M[3]), "zostało dodane!")
            elif x == "nie":
                K.append(imie)
                print("Imię żeńskie", (K[3]), "zostało dodane!")
            else:
                print("Koniec")
skrpyt_imiona()
































