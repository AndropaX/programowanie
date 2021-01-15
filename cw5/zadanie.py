import csv
import numpy as np
import urllib.request
import requests
import time
from datetime import datetime
from datetime import timedelta

def newlist():
    lista=[]
    np.array(lista)
    return lista

def checkurl(url):
    code=requests.get(url)
    if code.status_code==404:
        print("Niepoprawny kod stacji !")
        exit()

def openurl(url):
    cont=urllib.request.urlopen(url)
    return cont

def decode(url):
    lines=[l.decode('utf-8') for l in url.readlines()]
    return lines

def gettime(arg):
    curr=datetime.now()
    if arg==1:
        time=curr
    elif arg==2:
        time=curr.strftime("%m.%d.%Y-%H.%M")
    else:
        print("Niepoprawny argument !")
        exit()
    return time

def convtime(time):
    czas=datetime.strptime(time,"%d/%m/%Y %H:%M")
    return czas

def saveres(lista):
    time=gettime(2)
    filename="cw5/synop-"+time+".txt"
    with open(filename,'w') as f:
        for i in lista:
            f.write("%s\n" % i)
    print("Wyniki zostały zapisane do pliku o nazwie: ",filename)
    exit()

# Odczytywanie i wyświetlanie listy stacji
lista_st=newlist()
lisurl=openurl("https://danepubliczne.imgw.pl/api/data/synop/format/csv")
lin=decode(lisurl)
dane=csv.reader(lin)
next(dane)
for row in dane:
    lista_st.append(row)
tabl=np.array(lista_st)
print("Kod i nazwa stacji:")
for i in tabl:
   time.sleep(0.01)
   print(i[0],":",i[1])

# Wybór stacji
stacja=input("Wpisz kod stacji: ")
requrl="https://danepubliczne.imgw.pl/api/data/synop/id/"+stacja+"/format/csv"
checkurl(requrl)

# Określenie czasu działania
print("Obecna data i godzina:",gettime(2))
inlon=input("Wpisz datę do której ma działać skrypt w formacie DD/MM/RRRR hh:mm : ")
lon=convtime(inlon)
init=gettime(1)
cz_d=lon-init
print("Czas działania",lon-init)

#Zapisywanie pierwszej obserwacji
data=openurl(requrl)
int_cont=decode(data)
lista_dan=newlist()
data_dec=csv.reader(int_cont)
next(data_dec)
for row in data_dec:
    lista_dan.append(row)

#Czas działania <1h ?
mintime=timedelta(hours=1)
if cz_d<mintime:
    print("Czas działania skryptu jest krótszy niż godzina, zostanie zapisana jedna obserwacja")
    saveres(lista_dan)
else:
    print("Następna aktualizacja danych za: 1h")
    time.sleep(3600)

#Następne zapytania
while lon>gettime(1):
    lista_new=newlist()
    data2=openurl(requrl)
    new_cont=decode(data2)
    data_nd=csv.reader(new_cont)
    next(data_nd)
    for row in data_nd:
        lista_new.append(row)
    if lista_dan[-1][3]==lista_new[-1][3]:
        print("Brak nowych danych, następna aktualizacja za: 5 minut")
        time.sleep(300)
    else:
        print("Dostępne nowe dane")
    