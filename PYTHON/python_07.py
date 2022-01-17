import random


listes_pays = []
listes_capital = []

with open("pays.txt",  encoding="utf-8") as pays:

    for line in pays.readlines():
        l = line.split("#")
        if(len(l) == 2):
            listes_pays.append(l[0])
            listes_capital.append(l[1].replace("\n", ""))


question = random.randrange(len(listes_pays))
capital_responses = [question, random.randrange(len(listes_pays)),
                     random.randrange(len(listes_pays)), random.randrange(len(listes_pays))]

random.shuffle(capital_responses)
# QUESTION PRINCIPAL
print(f"Quel est la capital de {listes_pays[question]} : ")
# CHOIX Multiple
print("==============================")
print("Choisissez une bonne réponse ? ")
print(
    f"1. {listes_capital[capital_responses[0]]} 2.  {listes_capital[capital_responses[1]]}  3.  {listes_capital[capital_responses[2]]} 4.  {listes_capital[capital_responses[3]]} ")


# print(capital_responses)
