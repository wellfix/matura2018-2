plik1 = open("dane1.txt").read().split("\n")
plik2 = open("dane2.txt").read().split("\n")

for x in range(len(plik1)):
    plik1[x] = plik1[x].split()

for x in range(len(plik2)):
    plik2[x] = plik2[x].split()

ktore = []
licznik = 0

for x in range(1000):
    row1 = []
    row2 = []
    for y in plik1[x]:
        if y not in row1:
            row1.append(y)
    for y in plik2[x]:
        if y not in row2:
            row2.append(y)
    if row1 == row2:
        ktore.append(int(x) +1)
        licznik+=1
print("ile = "+ str(licznik) + " ktore = "+ str(ktore))


