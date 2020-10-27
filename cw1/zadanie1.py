wiek1=float(input("Wpisz wiek studenta 1: "))
wiek2=float(input("Wpisz wiek studenta 2: "))
if wiek1>wiek2:
    wynik='Student 1 jest starszy i ma '+str(int(wiek1))+' lat'
    print(wynik)
    with open('cw1/wiek1.txt','a') as plik:
        plik.write(wynik)
else:
    print('Student 1 nie jest starszy')