import zadanie1 as z1
temp=sum(z1.tablica[1:6,4].astype(float))/len(z1.tablica[1:6,4])
print("Średnia temperatura:",temp,"st. C")
humid=sum(z1.tablica[1:6,7].astype(float))/len(z1.tablica[1:6,7])
print("Średnia wilgotność względna:",humid,"%")
press=sum(z1.tablica[1:6,9].astype(float))/len(z1.tablica[1:6,7])
print("Średnie ciśnienie:",press,"hPa")