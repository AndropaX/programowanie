import csv
import numpy as np
import urllib.request
import requests
import time
from datetime import datetime
from datetime import timedelta
    
def writeurl(url):
    content=urllib.request.urlopen(url)
    lines=[l.decode('utf-8') for l in content.readlines()]
    data_list=[]
    np.array(data_list)
    data=csv.reader(lines)
    next(data)
    for row in data:
        data_list.append(row)
    return data_list

def getdataurl(station_number):
    ok=0
    while ok==0:
        url="https://danepubliczne.imgw.pl/api/data/synop/id/"+station_number+"/format/csv"
        code=requests.get(url)
        if code.status_code==404:
            print("Niepoprawny kod stacji !")
            station_number=input("Wpisz poprawny kod stacji: ")
        else:
            ok=1
    return url

def gettime(variant):
    current=datetime.now()
    if variant==1:
        time=current
    elif variant==2:
        time=current.strftime("%d/%m/%Y %H:%M")
    elif variant==3:
        date=current.strftime("%d/%m/%Y/%H")
        time_zero=datetime.strptime(date,"%d/%m/%Y/%H")
        time=time_zero+timedelta(hours=1)
    elif variant==4:
        time=current.strftime("%d.%m.%Y-%H.%M")
    else:
        raise ValueError("Niepoprawny argument !")   
    return time

def converttime(string):
    ok=0
    past=0
    while ok==0 or past==0:
        try:
            if datetime.strptime(string,"%d/%m/%Y %H:%M")<gettime(1):
                print("Data lub czas jest przeszły !")
                string=input("Wpisz poprawną datę i godzinę: ")
                past=0
            else:
                past=1
        except ValueError:
            print("Niepoprawny format daty i godziny !")
            string=input("Wpisz poprawną datę i godzinę: ")
            ok=0
        else:
            ok=1
    time=datetime.strptime(string,"%d/%m/%Y %H:%M")
    return time

def getsleeptime():
    while gettime(3)<gettime(1):
            time.sleep(1)
    hour_difference=gettime(3)-gettime(1)
    sleeptime=hour_difference.seconds+10
    return sleeptime

def saveresult(datalist,inittime):
    table=np.array(datalist)
    mean_temp=np.mean(table[:,4].astype(float))
    start_text=inittime.strftime("%d/%m/%Y %H:%M")
    finish_text=gettime(2)
    result_text="Średnia temperatura od "+start_text+" do "+finish_text+", z "+str(len(table))+" pomiarów, ze stacji "+str(table[0,1])+" wynosiła: "+str(mean_temp)+" st. C"
    print(result_text)
    file_time=gettime(4)
    filename="cw5/synop-"+file_time+".txt"
    with open(filename,'w') as f:
        for i in table:
            f.write("%s\n" % i)
        f.write(result_text)
    print("Wyniki zostały zapisane do pliku:",filename)
    exit()

# Odczytywanie i wyświetlanie listy stacji
station_list=writeurl("https://danepubliczne.imgw.pl/api/data/synop/format/csv")
station_table=np.array(station_list)
print("Kod i nazwa stacji:")
for i in station_table:
   time.sleep(0.01)
   print(i[0],":",i[1])

# Wybór stacji
station_input=input("Wpisz kod stacji: ")
request_url=getdataurl(station_input)

# Określenie czasu działania
print("Obecna data i godzina:",gettime(2))
time_input=input("Wpisz datę i godzinę do której ma działać skrypt w formacie DD/MM/RRRR hh:mm : ")
target_time=converttime(time_input)
init_time=gettime(1)
working_time=target_time-init_time
print("Czas działania skryptu:",working_time)

#Zapisywanie pierwszej obserwacji
data_list=writeurl(request_url)

#Zawieszenie działania do pełnej godziny
sleeptime=getsleeptime()
if working_time.seconds<sleeptime:
    print("Czas działania skryptu jest zbyt krótki, zostanie zapisana tylko jedna obserwacja")
    saveresult(data_list,init_time)
else:
    print("Pobrano pierwszą obserwację, następna aktualizacja danych za:",int(sleeptime/60),"minut")
    time.sleep(sleeptime)

#Następne zapytania
while target_time>gettime(1):
    new_data=writeurl(request_url)
    if data_list[-1][3]==new_data[-1][3]:
        print("Brak nowych danych, następna aktualizacja za: 5 minut")
        time.sleep(300)
    else:
        print("Pobrano nowe dane")
        for i in new_data:
            data_list.append(i)
        new_sleeptime=getsleeptime()
        remaining_time=target_time-gettime(1)
        if new_sleeptime>remaining_time.seconds:
            print("Pozostały czas działania jest zbyt krótki, kończenie działania skryptu")
            saveresult(data_list,init_time)
        else:
            print("Następna aktualizacja danych za:",int(new_sleeptime/60),"minut")
            time.sleep(new_sleeptime)

#Obliczanie średniej, zapisywanie wyników
print("Czas działania skryptu dobiegł końca")
saveresult(data_list,init_time)