def direBonjour(name):
	print(f"Bonjour {name}")

amis = "Jean Thierry Gustave".split()
tel = "79614036#61444953#79444953".split("#")

with open("phoneNumer.csv", 'r') as file:
	print(file.read())