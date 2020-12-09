with open("input.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


def totalNumBags(color):
    line = [' '.join(l.split()[4:])
            for l in lines if ' '.join(l.split()[:2]) == color][0].split(", ")

    if line[0] == "no other bags.":
        return 0
    counter = 0
    # append each child bag into an array, innerBags
    # recursively iterate through each color('s color color ....) in the array
    # add the result of numofbags + (numofbags * totalNumBags(color)) to counter
    innerBags = [' '.join(color.split()[:-1])
                 for color in line]  # [num bag, ...]
    for info in innerBags:
        numBags = info.split()[0]
        color = ' '.join(info.split()[1:])
        counter += int(numBags) + (totalNumBags(color) * int(numBags))
    return counter


print(totalNumBags("shiny gold"))
