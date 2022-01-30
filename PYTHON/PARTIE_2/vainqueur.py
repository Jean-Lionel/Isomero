import random
import uuid

friend_list = []

with open('contact.csv','w') as file:
	for i in range(20):
		number = random.randrange(700000000,800000000)
		name = uuid.uuid4()
		line = f"{name},{number} \n"
		file.write(line)
	