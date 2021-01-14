with open("input.txt") as f:
    line = f.readline().rstrip()
    lineLength = len(line)
    seatsArray = []
    seatsArray.append(['0'] * (lineLength+2))
    while line:
        if line.strip():
            seatsArray.append(['0'] + list(line) + ['0'])
        line = f.readline().rstrip()
    seatsArray.append(['0'] * (lineLength+2))


def countOccupiedSeats(arr):
    count = 0
    for r in range(1, len(arr)-1):
        for c in range(1, len(arr[r])-1):
            if arr[r][c] == "#":
                count += 1
    return count


def seeNextSeat(x, y, dx, dy):
    # return 0 if there's no seat
    # return 1 if there is an occupied seat
    # else we keep on going until we find a seat
    while 1:
        x += dx
        y += dy
        if ((x >= len(seatsArray)-1 or x < 0) or (y < 0 or y >= len(seatsArray[0])-1)):
            return 0
        if seatsArray[x][y] == "#":
            return 1
        elif seatsArray[x][y] == "L":
            return 0


# we compare to seatsArray and change the values of seatsArrayClone
seatsArrayClone = [row[:] for row in seatsArray]


def updateSeatsArrayClone(r, c):
    numOccupiedVisibleSeats = sum((seeNextSeat(r, c, 0, 1), seeNextSeat(r, c, 1, 0), seeNextSeat(
        r, c, 0, -1), seeNextSeat(r, c, -1, 0), seeNextSeat(r, c, 1, 1), seeNextSeat(r, c, 1, -1), seeNextSeat(r, c, -1, -1), seeNextSeat(r, c, -1, 1)))

    if seatsArray[r][c] == "L" and numOccupiedVisibleSeats == 0:
        seatsArrayClone[r][c] = "#"
    elif seatsArray[r][c] == "#" and numOccupiedVisibleSeats >= 5:
        seatsArrayClone[r][c] = "L"


while True:
    for r in range(1, len(seatsArrayClone)-1):
        for c in range(1, len(seatsArrayClone[r])-1):
            if seatsArray[r][c] != ".":
                updateSeatsArrayClone(r, c)
    # after we compare everything, we see if there was a change between the two arrays
    # if there was, we set em equal to one aonther and reloop
    # else, we count the number of occupied seats and that's our answer
    if seatsArray == seatsArrayClone:
        print(countOccupiedSeats(seatsArray))
        break
    else:
        seatsArray = [row[:] for row in seatsArrayClone]
