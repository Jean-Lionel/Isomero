# listes = [1,2,4,5,2]

# listes = listes + [ 42 ,85,74,14,25]
# listes.insert(1,100000);
# listes.append(24)
# listes.sort() # Ordonner un tableau

# hennok = ['a','b','a','x','aa']

# print(hennok.count('a'))
# hennok.reverse() # None
# print(hennok)

liste_pays = []
liste_capital = []
liste_continent = []
with open('data.txt', 'r') as file :
    for line in file.readlines():
        info = line.split("#")
        liste_pays.append(info[0])
        liste_capital.append(info[1])
        liste_continent.append(info[2])

print(liste_pays)
print(liste_capital)
print(liste_continent)