"""
Les modules sont des programmes Python qui contiennent des fonctions que l'on est amené à réutiliser souvent (on les appelle aussi bibliothèques ou libraries). Ce sont des « boîtes à outils » qui vont vous être très utiles.

Les développeurs de Python ont mis au point de nombreux modules qui effectuent une quantité phénoménale de tâches. Pour cette raison, prenez toujours le réflexe de vérifier si une partie du code que vous souhaitez écrire n'existe pas déjà sous forme de module.

La plupart de ces modules sont déjà installés dans les versions standards de Python. Vous pouvez accéder à une documentation exhaustive sur le site de Python. N'hésitez pas à explorer un peu ce site, la quantité de modules disponibles est impressionnante (plus de 300).
"""

# import random

# JEUX MATH QUIZ
# SERIE DE 3 QUESTION
# REPONSE 
# CALCULER
# point = 0
# limit = 3
# print("========== MATH QUIZ =========")
# for i in range(limit):
# 	a = random.randint(0,20)
# 	b = random.randint(0,20)
# 	reponse = int(input(f" Quel est le resultat de {a} + {b} = "))
# 	if reponse == (a + b):
# 		point += 5

# print(f"Vous avez obtenu {point} /  {limit *5}")

## POUR FAIRE DES CALCUL MATHEMATIQUE
import math

print(math.sin(45))
print(math.sqrt(81))

##Modul Courant 

## NOTE IMPORTANT 

    # math : fonctions et constantes mathématiques de base (sin, cos, exp, pi...).
    # sys : interaction avec l'interpréteur Python, passage d'arguments (cf. plus bas).
    # os : dialogue avec le système d'exploitation (cf. plus bas).
    # random : génération de nombres aléatoires.
    # time : accès à l'heure de l'ordinateur et aux fonctions gérant le temps.
    # urllib : récupération de données sur internet depuis Python.
    # Tkinter : interface python avec Tk. Création d'objets graphiques (cf. chapitre 20 Fenêtres graphiques et Tkinter).
    # re : gestion des expressions régulières (cf. chapitre 16 Expressions régulières et parsing*).
import random
x = [45,25,41,52,36,4]
random.shuffle(x)
print(x)
print(random.choice(x))
random.randrange()
random.ranint(12)