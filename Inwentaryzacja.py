import pandas as pd
def input_plik():
    sapl = pd.read_excel(input('Skopiuj ścieżke pliku SAP: '), header=None)
    b = sapl.iloc[:, 4].tolist()
    a = sapl.iloc[:, 5].tolist()
    a1 = [1 if pd.isna(k) else int(k) for k in a]
    b0 = [int(a) for a in b]
    b1 = [str(a) for a in b0]
    return b1,a1

def licz(sapl):
    sap,inw = sapl
    sap_check = []
    k = -1
    for numer in sap:
        k += 1
        if k > len(inw):
            sap_check.append(numer)
        elif inw[k] == 0:
            pass
        else:
            a = (numer).split(',') * inw[k]
            for numer in a:
                sap_check.append(numer)
    return sap_check

def porownaj(sap):
    sap_r = sap
    inwl = pd.read_excel(input('Skopiuj ścieżke pliku z inwentaryzacji: '), header=None)
    inw = inwl.iloc[:,0].tolist()
    inws = [int(a) for a in inw]
    inwt = [str(a) for a in inws]
    nadwyzka = []
    for a in inwt:
        if a in sap_r:
            sap_r.pop(sap_r.index(a))
        else:
            nadwyzka.append(a)
    return sap_r,nadwyzka

def zapisz(pliki):
    braki,nadwyzka = pliki
    s1 = pd.Series(braki)
    s2 = pd.Series(nadwyzka)
    df = pd.DataFrame({'Braki': s1, 'Nadwyżka': s2})
    df.to_excel(input('Wpisz ścieżke gdzie ma zostać zapisany plik podając na koniec \Inwentaryzacja.xlsx: '))
    return print('Wykonano, możesz wyłączyć program')
while True:
    try:
        sap = licz(input_plik())
        wynik = porownaj(sap)
        zapisz(wynik)
        break
    except(NameError,FileNotFoundError,PermissionError,OSError):
        print("Wpisz poprawnie lokalizacje pliku!")
    except(IndexError,ValueError,TypeError):
        print("Źle przygotowany plik lub zły plik!")
    except:
        print("Sprawdź instrukcję!")












