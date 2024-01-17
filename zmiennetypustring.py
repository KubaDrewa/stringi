#Zmienne typu string

# 1. Zmienne typu string są niemutowalne - nie można ich modyfikować
napis1 = 'informatyka'
''' napis1[2] = 's'
print(napis1) '''

#2. Indeksowanie znaków
print(napis1[2])
print(napis1[2:5])

# 3. Chodzenie po stringu w pętli
for z in napis1:
    print(z)

# 4. Zamiana napisu na listę
lista1 = list(napis1)
print(lista1)

# 5. Sprawdzanie, czy fragment wystęuje w słowie
napis2 = "Częstochowa"
if "stoch" in napis2:
    print("jest")
else:
    print("nie ma")

# 6. Wyrażenie listowe i napisy - ile liter "a" w słowie
napis3 = "konstantynopolitańczykówianeckza"
lista3 = [x for x in napis3 if x == "a"]
print(lista3, len(lista3))

# 7. Funkcja find()
napis5 = "ACCTCTCGGATCCAT"

print(napis5.find("TC"))  # od którego miejsca zaczyna się podany w nawiasie fragment

print(napis5.find("TC", 8, 14))
                          # funkcja szuka elementu w konkretnym przedziale (od id= 8 do 14)
indeksy = []
gdzie = -1

while gdzie < len(napis5):
    gdzie = napis5.find('TC', gdzie+1)
    if gdzie == -1:
        break
    indeksy.append(gdzie)
print(indeksy)