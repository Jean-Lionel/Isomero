import random

miniscule = "abcdefghijklmnopqrstuvwxyz"
majuscule = miniscule.upper()
nombre = "0123456789"
caracter_speciaux = "!@#$%^&*()+_=][?.,/"

chaine = miniscule + majuscule + nombre + caracter_speciaux
longuer = 16
password = "".join(random.sample(chaine,longuer))
print(f"Le mot de passe est {password}")


