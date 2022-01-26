
with open("hello.txt", "w") as f:
    for i in range(100):
        line = "{} => {} \n".format(i, i**2)
        f.write(line)
