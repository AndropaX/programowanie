wiek1=float(input("Wpisz wiek studenta 1: "))
wiek2=float(input("Wpisz wiek studenta 2: "))
if wiek1>wiek2:
    wiekw=str(int(wiek1))
    tekstp='Student 1 jest starszy i ma: '
    tekstk=' lat'
    print(tekstp,wiekw,tekstk)
    wynik=tekstp,wiekw,tekstk
    with open('wiek1.txt','a') as plik:
        plik.write(''.join(wynik))
else:
    print('Student 1 nie jest starszy')