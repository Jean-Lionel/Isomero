# animaux = ["girafe", "tigre", "singe", "souris"]

# # FUNCTION len kugira umenye taille ya tableau
# # extension AREPL

# print(len(animaux))

# # FUNCTION range kugira umenya ibiri muri interavalle
# print(range(0, 100, 4))
# # debut=0 , Fin , pas=1

# # FUNCTION list kugira umenya ibiri muri interavalle

# print(list(range(0, 10, 1)))
# print(list(range(4)))

# animaux_2 = [["girafe", "herbivore"], ["tigre", "carnivole"]]
# print(animaux_2[0])

# nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 45, 20, 7, -1]
# # Afficher le Minimum
# print(min(nombres))
# # afficher le max
# print(max(nombres))

# print(nombres[13])

""" Affichez la table de multiplication par 9 en une seule commande avec les instructions range() et list(). """

table_de_multiplication_9 = list(range(0, 100, 9))

""" Combien y a-t-il de nombres pairs dans l'intervalle [2, 10000] inclus ?"""

liste_tableau = len(list(range(2, 10000, 2)))

print(f"Le nombre total est de {liste_tableau}")
