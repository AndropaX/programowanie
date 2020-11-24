import numpy as np
import zadanie1 as z1
temp=np.mean(z1.tablica[1:6,4].astype(float))
print("Średnia temperatura:",temp,"st. C")
humid=np.mean(z1.tablica[1:6,7].astype(float))
print("Średnia wilgotność względna:",humid,"%")
press=np.mean(z1.tablica[1:6,9].astype(float))
print("Średnie ciśnienie:",press,"hPa")