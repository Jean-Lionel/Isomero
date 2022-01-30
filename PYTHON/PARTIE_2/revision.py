import random 
import string

liste_pays = []

with open("list_pays.txt", 'r', encoding = "utf8") as file:
	for line in file.readlines():
		liste_pays.append(line.split("#"))


for i in range(5):
	q = random.randint(0,len(liste_pays)-1)
	print(f"reponse est {liste_pays[q][1]}")
	response = input(f"Quel est la capital du {liste_pays[q][0]} ? : ")


	if  response.lower().strip() == liste_pays[q][1].lower().strip():
		print("Filicitation vous avez reussi")
	else:
		print(f"Echeque c'est {liste_pays[q][1]}")