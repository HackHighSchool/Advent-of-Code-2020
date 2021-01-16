import math

with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines if line.strip()]
    lines[1] = [int(i) for i in lines[1].split(",") if i != "x"]

timestamp = float(lines[0])
buses = lines[1]

difference = [buses[0] * math.ceil(timestamp/buses[0]), buses[0]]
# difference[0] is the closest factor of the busID to the timestamp
# difference[1] is the busID
for n in range(1, len(buses)):
    busNum = buses[n]
    diff = difference[0]
    busNum *= math.ceil(timestamp/busNum)
    if busNum >= timestamp and busNum - timestamp < diff:
        difference = [busNum - timestamp, buses[n]]
print(int(difference[0] * difference[1]))
