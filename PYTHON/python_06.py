# L = 20

# for i in range(L):
#     for j in range(1, (L - i + 1)):
#         print(" ", end="")
#     for j in range(1, 2*i):
#         print("*", end="")
#     print()

# taille = 20

# for i in range(taille):
#     for j in range(1, taille-i):
#         print(" ", end="")

#     for j in range(1, 2 * i):
#         print("*", end="")
#     print()

# animaux = ["girafe", "tigre", "singe", "souris"]

# for animal in animaux:
#     print(animal, end="\t")

# exemple  IGISORO
#print(list(range(0, 8, 1)))

# for i in range(12):
#     for j in range(12):
#         print(f" {i} X {j} = {i * j}")

#     print("_____________")


for i in range(1, 10, 1):
    for j in range(i):
        print("*", end="")
    print()

for i in range(1, 10, -1):
    for j in range(i):
        print("*", end="")
    print()
