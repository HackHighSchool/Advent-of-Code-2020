import math

with open("input.txt") as f:
    lines = f.readlines()
    del lines[0]
    lines = [line.rstrip() for line in lines[0].split(",") if line.strip()]
    print(lines)


for i in range(len(lines)):
    busID = lines[i]
    if busID == "x":
        continue
