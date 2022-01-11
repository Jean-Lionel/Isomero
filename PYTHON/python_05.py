# animaux = ["girafe", "tigre", "singe", "souris"]

# # boucle For
# for animal in animaux:
#     print(animal)

# # boucle for avec la function range
# for i in range(10):
#     print(i)

# debut = 0
# # Boucle While

# while debut < 10:
#     print(debut)
#     debut += 1


""" UMWIMENYEREZO IGISORO AVEC FOR ET AVEC WHILE """

# for i in range(0, 12):
#     for j in range(0, 12):
#         print(f" {i} X {j} = {i * j}")

#     print("===============")


"""
*
**
***
****
*****
******
*******
********
*********
**********

"""

# for i in range(10):
#     for j in range(i):
#         print("*", end="")
#     print("")

"""
A FAIRE
**********
*********
********
*******
******
*****
****
***
**
*
"""

# for i in range(10, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print("")

""" 
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************

"""

"""IGISORO HAMWE NA WHILE"""

i = 0
j = 0

while i < 12:
    while j < 12:
        print(f" {i} X {j} = {i * j}")
        j += 1
    print("=========")
    j = 0
    i += 1
