import pandas as pd
def input_plik():
    sapl = pd.read_excel(r'C:\Users\Prosik\Downloads\Raport_ST_MAG_20220122T141811.xlsx', header=None)
    seria = sapl.iloc[:, 4].tolist()
    ilosc = sapl.iloc[:, 5].tolist()
    nazwa = sapl.iloc[:, 0].tolist()
    ilosc_int = [1 if pd.isna(k) else int(k) for k in ilosc]
    b0 = ["None" if pd.isna(a) else int(a) for a in seria]
    seria_string = [str(a) for a in b0]
    return seria_string,ilosc_int

def licz(nazwa):
    sap,inw = nazwa
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
    inwl = pd.read_excel(r'C:\Users\Prosik\Downloads\Raport.xlsx', header=None)
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

print(licz(input_plik()))





