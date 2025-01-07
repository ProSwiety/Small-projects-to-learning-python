import pandas as pd
import xlsxwriter
def sap():
    lok = input('Skopiuj lokalizacje pliku SAP: ')
    lok += ".xlsx"
    plik_sap = pd.read_excel(lok, header=None)
    nazwa_produkt = plik_sap.iloc[:, 0].tolist()
    numer_seryjny = plik_sap.iloc[:, 4].tolist()
    ilosc_produkt = plik_sap.iloc[:, 5].tolist()
    return nazwa_produkt, numer_seryjny, ilosc_produkt

def skan():
    lok = input('Skopiuj lokalizacje pliku z Inwentaryzacji: ')
    lok += ".xlsx"
    plik_skan = pd.read_excel(lok, header=None)
    numer_seryjny_orygginal = plik_skan.iloc[:, 0].tolist()
    numer_seryjny_int = [int(x) for x in numer_seryjny_orygginal]
    return numer_seryjny_int

def dic_file(listy):
    nazwa, numer, ilosc = listy
    dic_sap_nazwa = {}
    dic_sap_ilosc = {}
    licznik = -1
    for x in nazwa:
        licznik += 1
        dic_sap_nazwa[x] = numer[licznik]
    licznik = -1
    for x in nazwa:
        licznik += 1
        dic_sap_ilosc[x] = ilosc[licznik]
    return dic_sap_nazwa,dic_sap_ilosc

def porownaj(dic_sap,skan):
    seria,ilosc = dic_sap
    skan = skan
    new_ilosc = {}
    nadwyzka = {}
    beznazwy = {}
    numerate = -1
    lista = [seria for nazwa, seria in seria.items()]
    for x in skan:
        if x not in lista:
            if x not in beznazwy.values():
                numerate += 1
                beznazwy[f"Bez nazwy{numerate}"] = x
                new_ilosc[f'Bez nazwy{numerate}'] = -1
            else:
                for a in range(0,100):
                    if x == beznazwy.get(f'Bez nazwy{a}'):
                        new_ilosc[f'Bez nazwy{a}'] -= 1

    for produkt, numer in seria.items():
        for x in skan:
            if numer == x:
                ilosc[produkt] -= 1
    for nazwa1,numer in ilosc.items():
        if numer != 0:
            new_ilosc[nazwa1] = numer
        else:
            seria.pop(nazwa1)
    for nazwa2,ilosc in new_ilosc.items():
        if ilosc < 0:
            nadwyzka[nazwa2] = ilosc * -1
        if ilosc > 0:
            new_ilosc[nazwa2] = ilosc * -1
    for nazwa3, ilosc in nadwyzka.items():
        if nazwa3 in new_ilosc.keys():
            new_ilosc.pop(nazwa3)
    for nazwa,numer_seryjny in beznazwy.items():
        seria[nazwa] = numer_seryjny

    return new_ilosc,nadwyzka,seria

def zapisz(pliki):
    braki,nadwyzka,seria = pliki
    s1 = pd.Series(seria)
    s2 = pd.Series(nadwyzka)
    s3 = pd.Series(braki)
    df = pd.DataFrame({"Numer Seryjny  ": s1,"Braki ": s3," Nadwyżka ": s2})
    lok = input('Wpisz ścieżke gdzie ma zostać zapisany plik podając na koniec \Wynik: ')
    lok += ".xlsx"
    df.to_excel(lok)
    return print("Możesz wyłączyć program.")

print("Wciśnij enter...")
while True:
    try:
        pliki = porownaj(dic_file(sap()),skan())
        zapisz(pliki)
        break
    except(NameError,FileNotFoundError,PermissionError,OSError):
        print("Wpisz poprawnie lokalizacje pliku!")
    except(IndexError,ValueError,TypeError):
        print("Źle przygotowany plik lub zły plik!")
    except:
        print("Sprawdź instrukcję!")




