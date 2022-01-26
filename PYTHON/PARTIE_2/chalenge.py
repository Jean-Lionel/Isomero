import matplotlib.pyplot as plt

x = []
y = []
with open("sin2ori.dat", "r") as f_in:
    for line in f_in:
        coords = line.split()
        x.append(float(coords[0]))
        y.append(float(coords[1]))
plt.figure(figsize=(8,8))
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("Distance de sin(x)à l'origine")
plt.savefig("sin2ori.png")