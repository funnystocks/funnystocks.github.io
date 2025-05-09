file = open("computers.csv", "r")
lines = [l.rstrip() for l in file]
lines.pop(0)
file.close()
print(lines)