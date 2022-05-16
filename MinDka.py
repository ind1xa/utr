import sys
import numpy as np

skupStanjaStr = sys.stdin.readline().rstrip('\n')
skupStanjaList1 = skupStanjaStr.split(',')

skupAbecedeStr = sys.stdin.readline().rstrip('\n')
skupAbecedeList = skupAbecedeStr.split(',')

prihvatljivaStanjaStr = sys.stdin.readline().rstrip('\n')
prihvatljivaStanjaList = prihvatljivaStanjaStr.split(',')

pocetnoStanje = sys.stdin.readline().rstrip('\n')

listaPrijelaza1 = []

for line in sys.stdin:
    line = line.rstrip('\n')
    pomocnaLista = line.split('->')
    pomocnaLista2 = pomocnaLista[0].split(',')
    listaOd3 = []
    if(pomocnaLista2[0] in skupStanjaList1):
        listaOd3.append(pomocnaLista2[0])
    if(pomocnaLista2[1] in skupAbecedeList):
        listaOd3.append(pomocnaLista2[1])
    if(pomocnaLista[1] in skupStanjaList1):
        listaOd3.append(pomocnaLista[1])
    if (len(listaOd3) == 3):
        listaPrijelaza1.append(listaOd3)


#---------------------------------------------------------

#Uklanjanje nedohvatljivih stanja
listaDohvatljivihStanja = []
listaDohvatljivihStanja.append(pocetnoStanje)

biloPromjene = True
while(biloPromjene):
    biloPromjene = False
    for x in listaPrijelaza1:
        if (x[0] in listaDohvatljivihStanja):
            if(x[2] not in listaDohvatljivihStanja):
                listaDohvatljivihStanja.append(x[2])
                biloPromjene = True

skupStanjaList = skupStanjaList1.copy()
listaPrijelaza = listaPrijelaza1.copy()

for x in skupStanjaList1:
    if (x not in listaDohvatljivihStanja):
        if (x in skupStanjaList):
            skupStanjaList.remove(x)
        if (x in prihvatljivaStanjaList):
            prihvatljivaStanjaList.remove(x)
        for y in listaPrijelaza1:
            if (y[0] == x):
                if (y in listaPrijelaza):
                    listaPrijelaza.remove(y)


#Određivanje istovjetnih stanja:
matricaNeistovjetnih = np.zeros((len(skupStanjaList),len(skupStanjaList)))

for x in range(0, len(skupStanjaList)):
    for y in range(0,x):
        if ((skupStanjaList[x] in prihvatljivaStanjaList and skupStanjaList[y] not in prihvatljivaStanjaList) 
        or (skupStanjaList[x] not in prihvatljivaStanjaList and skupStanjaList[y] in prihvatljivaStanjaList)):
            matricaNeistovjetnih[x][y] = 1
        
biloPromjene = True
while (biloPromjene):
    biloPromjene = False
    for x in range(0, len(skupStanjaList)):
        for y in range(0,x):
            if (matricaNeistovjetnih[x][y] == 0):
                for z in range(0, len(skupAbecedeList)):
                    prijelazx = listaPrijelaza[x*len(skupAbecedeList)+z]
                    prijelazy = listaPrijelaza[y*len(skupAbecedeList)+z]
                    if ((prijelazx[2] in prihvatljivaStanjaList and prijelazy[2] not in prihvatljivaStanjaList)
                    or (prijelazx[2] not in prihvatljivaStanjaList and prijelazy[2] in prihvatljivaStanjaList)):
                        matricaNeistovjetnih[x][y] = 1
                        biloPromjene = True
                    if (matricaNeistovjetnih[skupStanjaList.index(prijelazx[2])][skupStanjaList.index(prijelazy[2])] == 1):
                        matricaNeistovjetnih[x][y] = 1
                        biloPromjene = True

noviSkupStanja = skupStanjaList.copy()
novaListaPrijelaza = listaPrijelaza.copy()

for x in range(0, len(skupStanjaList)):
    for y in range(0,x):
        if (matricaNeistovjetnih[x][y] == 0):
            stanjex = skupStanjaList[x]
            stanjey = skupStanjaList[y]
            if (stanjex in noviSkupStanja):
                noviSkupStanja.remove(stanjex)
            if (stanjex in prihvatljivaStanjaList):
                prihvatljivaStanjaList.remove(stanjex)
            if (pocetnoStanje == stanjex):
                pocetnoStanje = stanjey
            for z in listaPrijelaza:
                if (z[0] == stanjex):
                    if (z in novaListaPrijelaza):
                        novaListaPrijelaza.remove(z)
                if (z[2] == stanjex):
                    z[2] = stanjey


stanjaPrint = ""
for x in noviSkupStanja:
    stanjaPrint = stanjaPrint + x + ","
stanjaPrint = stanjaPrint[:-1]
#stanjaPrint = stanjaPrint + '\n'
print(stanjaPrint)

print(skupAbecedeStr)

prihvatljivaStanjaPrint = ""
for x in prihvatljivaStanjaList:
    prihvatljivaStanjaPrint = prihvatljivaStanjaPrint + x + ","
prihvatljivaStanjaPrint = prihvatljivaStanjaPrint[:-1]
print(prihvatljivaStanjaPrint)

print(pocetnoStanje)
for x in novaListaPrijelaza:
    prijelaziPrint = x[0] + "," + x[1] + "->" + x[2]
    print(prijelaziPrint)