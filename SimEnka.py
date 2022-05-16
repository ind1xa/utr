import sys

def dohvatiNovoStanje(velikaLista, stanja, znak):
    rezultat = {*()}
    for stanje in stanja:
        for x in velikaLista:
            if (x[0] == stanje and x[1] == znak):
                for y in range (2, len(x)):
                    rezultat.add(x[y])
 
    return rezultat;

def dodajEpsilone(velikaLista, set):
    setKopija = set.copy()
    for y in setKopija:
        for x in velikaLista:
            #print(x[0], y, x[1])
            if (x[0] == y and x[1] == '$'):
                for z in range (2, len(x)):
                    set.add(x[z])
    
    if (len(setKopija) != len(set)):
        dodajEpsilone(velikaLista, set)
    
    return set;


ulazniNizoviStr = sys.stdin.readline().rstrip('\n')
ulazniNizoviLStr = ulazniNizoviStr.split('|')       #lista ulaznih nizova
ulazniNizoviLista = [];
for x in range (len(ulazniNizoviLStr)):
    novaLista = ulazniNizoviLStr[x].split(',')
    ulazniNizoviLista.append(novaLista)

skupStanjaStr = sys.stdin.readline().rstrip('\n')
skupStanjaList = skupStanjaStr.split(',')

skupAbecedeStr = sys.stdin.readline().rstrip('\n')
skupAbecedeList = skupAbecedeStr.split(',')
skupAbecedeList.append('$')

prihvatljivaStanjaStr = sys.stdin.readline().rstrip('\n')
prihvatljivaStanjaList = prihvatljivaStanjaStr.split(',')

pocetnoStanje = sys.stdin.readline().rstrip('\n')

velikaLista = []

for line in sys.stdin:
    listaSZS = []           #lista: stanje, znak, [stanja]...
    line = line.rstrip('\n')
    pomocnaLista = line.split('->')
    listaSZS.append(pomocnaLista[0].split(',')[0])
    if (pomocnaLista[0].split(',')[1] in skupAbecedeList):
        listaSZS.append(pomocnaLista[0].split(',')[1])
    counter = 0
    for x in range (len(pomocnaLista[1].split(','))):
        counter = counter + 1
        if (pomocnaLista[1].split(',')[x] in skupStanjaList):
            listaSZS.append(pomocnaLista[1].split(',')[x])
    
    if (len(listaSZS) == counter + 2):
        velikaLista.append(listaSZS)

#---------------------------------------------------------


for x in ulazniNizoviLista:
    pocetniSet = {pocetnoStanje}
    trenutnoStanje = list(dodajEpsilone(velikaLista, pocetniSet))
    trenutnoStanje.sort()
    izlaz = ''
    for i in range (len(trenutnoStanje)):
        izlaz = izlaz + trenutnoStanje[i]
        if (i != len(trenutnoStanje)-1):
            izlaz = izlaz + ','
    izlaz = izlaz + '|'
    for y in x:
        if (y not in skupAbecedeList): break
        setPrijelaza = dohvatiNovoStanje(velikaLista, trenutnoStanje, y)
        trenutnoStanje.clear()
        trenutnoStanje = list(dodajEpsilone(velikaLista, setPrijelaza))
        trenutnoStanje.sort()
        if (len(trenutnoStanje) == 0):
            izlaz = izlaz + '#'
        for z in range (len(trenutnoStanje)):
            izlaz = izlaz + trenutnoStanje[z]
            if (z != len(trenutnoStanje)-1):
                izlaz = izlaz + ','
        izlaz = izlaz + '|'
    izlaz = izlaz[:-1] #+ "\n"
    print(izlaz)