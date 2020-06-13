plik1 = open("dane1.txt").read().split("\n")
plik2 = open("dane2.txt").read().split("\n")

for x in range(len(plik1)):
    plik1[x] = plik1[x].split()

for x in range(len(plik2)):
    plik2[x] = plik2[x].split()
licznik = 0
for x in range(len(plik1)):
    if plik1[x][9] == plik2[x][9]:
        licznik+=1

print(licznik)