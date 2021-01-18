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
    
def openurl(url):
    code=requests.get(url)
    if code.status_code==404:
        print("Niepoprawny kod stacji !")
        exit()
    cont=urllib.request.urlopen(url)
    lines=[l.decode('utf-8') for l in cont.readlines()]
    return lines

def gettime(arg):
    curr=datetime.now()
    if arg==1:
        time=curr
    elif arg==2:
        time=curr.strftime("%d.%m.%Y-%H.%M")
    elif arg==3:
        time=curr.strftime("%d/%m/%Y %H:%M")
    elif arg==4:
        date=curr.strftime("%d/%m/%Y/")
        hour=int(curr.strftime("%H"))+1
        combined=date+str(hour)
        time=datetime.strptime(combined,"%d/%m/%Y/%H")
    else:
        print("Niepoprawny argument !")
        exit()
    return time

def getsleeptime():
    hourdiff=gettime(4)-gettime(1)
    sleeptime=hourdiff.seconds
    return sleeptime

def convtime(time):
    ok=0
    past=0
    while ok==0 or past==0:
        try:
            datetime.strptime(time,"%d/%m/%Y %H:%M")
            if datetime.strptime(time,"%d/%m/%Y %H:%M")<gettime(1):
                print("Data lub czas jest przeszły !")
                time=input("Wpisz poprawną datę: ")
                past=0
            else:
                past=1
        except ValueError:
            print("Niepoprawna data !")
            time=input("Wpisz poprawną datę: ")
            ok=0
        else:
            ok=1
    czas=datetime.strptime(time,"%d/%m/%Y %H:%M")
    return czas

def calcmeantemp(lista):
    table=np.array(lista)
    temp=np.mean(table[:,4].astype(float))
    temp_text="Średnia temperatura z "+str(len(table))+" pomiarów, ze stacji "+str(table[0,1])+" wynosiła: "+str(temp)+" st. C"
    print(table)
    print(temp_text)
    return temp_text

def saveres(lista):
    output=calcmeantemp(lista)
    time=gettime(2)
    filename="cw5/synop-"+time+".txt"
    with open(filename,'w') as f:
        f.write(output)
        #for i in comp_list:
        #    f.write("%s\n" % i)
    print("Wyniki zostały zapisane do pliku:",filename)
    exit()

# Odczytywanie i wyświetlanie listy stacji
lista_st=newlist()
lisurl=openurl("https://danepubliczne.imgw.pl/api/data/synop/format/csv")
dane=csv.reader(lisurl)
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
data=openurl(requrl)

# Określenie czasu działania
print("Obecna data i godzina:",gettime(3))
inlon=input("Wpisz datę do której ma działać skrypt w formacie DD/MM/RRRR hh:mm : ")
lon=convtime(inlon)
init=gettime(1)
cz_d=lon-init
print("Czas działania:",cz_d)

#Zapisywanie pierwszej obserwacji
lista_dan=newlist()
data_dec=csv.reader(data)
next(data_dec)
for row in data_dec:
    lista_dan.append(row)

#Zawieszenie działania do pełnej godziny
sleeptime=getsleeptime()
if cz_d.seconds<sleeptime:
    print("Czas działania skryptu jest zbyt krótki, zostanie zapisana tylko jedna obserwacja")
    saveres(lista_dan)
else:
    print("Pobrano pierwszą obserwację, następna aktualizacja danych za:",int(sleeptime/60),"minut")
    time.sleep(sleeptime)

#Następne zapytania
while lon>gettime(1):
    lista_new=newlist()
    data2=openurl(requrl)
    data_nd=csv.reader(data2)
    next(data_nd)
    for row in data_nd:
        lista_new.append(row)
    if lista_dan[-1][3]==lista_new[-1][3]:
        print("Brak nowych danych, następna aktualizacja za: 5 minut")
        time.sleep(300)
    else:
        new_sleep=getsleeptime()
        rem_time=lon-gettime(1)
        print("Pobrano nowe dane")
        for i in lista_new:
            lista_dan.append(i)
        if new_sleep>rem_time.seconds:
            print("Pozostały czas działania jest zbyt krótki, kończenie działania")
            saveres(lista_dan)
        else:
            print("Następna aktualizacja danych za:",int(new_sleep/60),"minut")
            time.sleep(new_sleep)

#Obliczanie średniej, zapisywanie wyników
print("Czas działania skryptu dobiegł końca")
saveres(lista_dan)   