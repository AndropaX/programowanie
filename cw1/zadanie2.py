wiek1=float(input("Wpisz wiek studenta 1: "))
with open('cw1/wiek_drugiego_studenta.txt') as plik:
    wiek2=float(plik.read())
if wiek1<wiek2:
    diff=wiek2-wiek1
    wynik='Pierwszy student jest młodszy od studenta drugiego o '+str(int(diff))+' lat'
    print(wynik)
    with open('cw1/wiek2.txt','a') as plik:
        plik.write(wynik)
else:
    print('Student 1 nie jest młodszy')