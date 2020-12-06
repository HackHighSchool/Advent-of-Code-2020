file = open("day1entries.txt", "r")

entries = []

#Variables to track the two correct numbers, and their product
num1 = 0
num2 = 0
product = 0

for line in file:
    entries.append(int(line))

file.close()

#Track 2 numbers in the list of numbers, by index
for x in range(len(entries)):
    for y in range(len(entries)):

        #Evaluate sum and make sure entry indices are not the same
        if entries[x]+entries[y] == 2020 and x != y:
            num1 = entries[x]
            num2 = entries[y]
            product = entries[x]*entries[y]
            break

#Output results
print("Number 1: {}".format(num1))
print("Number 2: {}".format(num2))
print("Product: {}".format(product))
