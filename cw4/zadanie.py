import csv
import numpy as np
import glob
import os

lista=[]
np.array(lista)
katalog='cw4'
for filename in glob.glob(os.path.join(katalog,'*.csv')):
    with open(os.path.join(os.getcwd(), filename),'r',encoding="utf8") as f:
        dane=csv.reader(f)
        #ignore headers
        next(dane)
        for row in dane:
            lista.append(row)
tablica=np.array(lista)
temperatura=tablica[:,4].astype(float)
min_temp=min(temperatura)
minim=np.where(temperatura==min_temp)
print("Stacja z minimalnym pomiarem temperatury:",tablica[minim,1][0][0])
print("Godzina minimalnego pomiaru temperatury:",tablica[minim,3][0][0])
max_temp=max(temperatura)
maxim=np.where(temperatura==max_temp)
print("Stacja z maksymalnym pomiarem temperatury:",tablica[maxim,1][0][0])
print("Godzina maksymalnego pomiaru temperatury:",tablica[maxim,3][0][0])
opad=tablica[:,8].astype(float)
opad_t=np.where(0<opad)
print("Stacje i godziny na których odnotowano opad:")
for i in opad_t:
    print(tablica[i,1])
    print(tablica[i,3])
