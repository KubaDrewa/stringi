plik = open('dane.txt')
dane = plik.readlines()
print(dane)
dane = [l.strip() for l in dane]
print(dane)

licznik = 0

for l in dane:
    if  l[0] == l[-1]:
        licznik += 1
print(licznik)


licznik = 0

for l in dane:
    l_10 = str(int(l, 8))
    if l_10[0] == l_10[-1]:
        licznik += 1
print(licznik)


licznik = 0
for l in dane:
    l_lista = list(l)
    l_kopia_lista = l_lista[::]
    l_kopia_lista.sort()
    if l_lista == l_kopia_lista:
        licznik += 1

print(licznik)