import matplotlib.pyplot as plt

x = []
y = []
with open("spirale.dat", "r") as f_in:
    for line in f_in:
        coords = line.split()
        x.append(float(coords[0]))
        y.append(float(coords[1]))

plt.figure(figsize=(8, 8))
mini = min(x+y) * 1.2
maxi = max(x+y) * 1.2
plt.xlim(mini, maxi)
plt.ylim(mini, maxi)
plt.plot(x, y)
plt.savefig("spirale.png")
