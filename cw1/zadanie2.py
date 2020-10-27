wiek1=int(input("Wpisz wiek studenta 1: "))
with open('cw1/wiek_drugiego_studenta.txt','r') as plik:
    wiek2=int(plik.read())
if wiek1<wiek2:
    diff=wiek2-wiek1
    wynik='Pierwszy student jest młodszy od studenta drugiego o '+str(diff)+' lat'
    print(wynik)
    with open('cw1/wiek2.txt','w') as plik:
        plik.write(wynik)
else:
    print('Student 1 nie jest młodszy')