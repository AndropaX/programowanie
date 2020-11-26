import numpy as np
import csv
lista=[]
np.array(lista)
with open('cw3/meteo.csv','r') as plikcsv:
    zmienna=csv.reader(plikcsv)
    for row in zmienna:
        lista.append(row)
nagl=list(lista[0])
print("Lista nagłówków:",nagl)        
tablica=np.array(lista)
print("Dane w 4 wierszu:",tablica[3])
print("Miejscowość w wierszu nr. 4:",tablica[3][1])