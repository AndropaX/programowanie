import csv
import numpy as np
import urllib.request
import requests
import time
from datetime import datetime

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

def gettime():
    curr=datetime.now()
    dattime=curr.strftime("%d/%m/%Y %H:%M")
    print(curr)
    return dattime

lista_st=[]
np.array(lista_st)
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
stacja=input("Wpisz kod stacji: ")
requrl="https://danepubliczne.imgw.pl/api/data/synop/id/"+stacja+"/format/csv"
checkurl(requrl)
data=openurl(requrl)
print(data.read())
init=gettime()
print("Obecna data i godzina:",init)
lon=input("Wpisz datę do której ma działać skrypt w formacie DD/MM/RRRR hh:mm : ")
if lon<init:
    print("mniejszy")
else:
    print("większy")