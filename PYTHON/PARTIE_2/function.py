# def direBonjour():
# 	print("Bonjour")

# def direBonjourA(izina):
# 	print(f"Bonjour {izina}")

# def care(nombre):
# 	return nombre ** 2

# def cube(nombre):
# 	return nombre ** 3

# def multiplier(a, b):
# 	return a * b

# surfaceCarre = care(12)

# name = direBonjourA("JEAN")

# print(f"Le care de {12} est {surfaceCarre}")

# def perimetre(largeur , nombre_cote =4):
# 	return largeur * nombre_cote

# p = perimetre(4,8)

# print(f"perimetre est de {p}")


# a = 8

# def nombreEcrit():
# 	x = 80
# 	print(a)
# 	print(x)

# nombreEcrit()

def countTo(nombre):
	for i in range(nombre):
		print(f"count No {i}")
	print("===================")


def increaseValue(number):
	print(f"count No {number}")
	if(number > 0):
		return increaseValue(number - 1)

increaseValue(100)


# ECRIRE UNE FONCTION VERIFIANT SI UN NOMBRE DONNE EST PREMIER

1.2.3.5.7.11.13.17.19.23.29.31.....