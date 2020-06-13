plik1 = open("dane1.txt").read().split("\n")
plik2 = open("dane2.txt").read().split("\n")

for x in range(len(plik1)):
    plik1[x] = plik1[x].split()

for x in range(len(plik2)):
    plik2[x] = plik2[x].split()

licznik = 0

for x in range(1000):
    parz1 = 0
    parz2 = 0
    for y in range(10):
        if int(plik1[x][y]) % 2 == 0:
            parz1 = parz1 + 1
        if int(plik2[x][y]) % 2 == 0:
            parz2 = parz2 + 1
    if parz1 == 5 and parz2 == 5:
        licznik+=1

print(licznik)