#nombre = int(input("Entre un Nombre + : "))

def isPremier(nombre : int):
	i = 2 
	while (i < nombre) and (nombre %i != 0):
		i += 1
	if i == nombre:
		return True
	else:
		return False
