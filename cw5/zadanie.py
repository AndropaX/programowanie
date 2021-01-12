import csv
import numpy as np
import urllib.request
import requests
import time

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

lista_st=[]
np.array(lista_st)
lisurl=urllib.request.urlopen("https://danepubliczne.imgw.pl/api/data/synop/format/csv")
lin=decode(lisurl)
dane=csv.reader(lin)
next(dane)
for row in dane:
    lista_st.append(row)
tabl=np.array(lista_st)
print("Kod i nazwa stacji:")
for i in tabl:
   time.sleep(0.1)
   print(i[0],":",i[1])
stacja=input("Wpisz kod stacji: ")
requrl="https://danepubliczne.imgw.pl/api/data/synop/id/"+stacja+"/format/csv"
checkurl(requrl)
data=urllib.request.urlopen(requrl)
print(data.read())