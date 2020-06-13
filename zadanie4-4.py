plik1 = open("dane1.txt").read().split("\n")
plik2 = open("dane2.txt").read().split("\n")

for x in range(len(plik1)):
    plik1[x] = plik1[x].split()

for x in range(len(plik2)):
    plik2[x] = plik2[x].split()


for x in range(1000):
    wynik = []
    for y in range(10):
        wynik.append(int(plik1[x][y]))
    for y in range(10):
        wynik.append(int(plik2[x][y]))
    wynik.sort()
    wynik = str(wynik).replace(",","")
    print(wynik[1:len(wynik)-1])


