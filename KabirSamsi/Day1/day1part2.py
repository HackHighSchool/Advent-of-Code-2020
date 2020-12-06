file = open("day1entries.txt", "r")
entries = []

#Variables to track the three correct numbers, and their product
num1 = 0
num2 = 0
num3 = 0
product = 0

for line in file:
    entries.append(int(line))

file.close()

#Track 3 numbers in the list of numbers, by index
for x in range(len(entries)):
    for y in range(len(entries)):
        for z in range(len(entries)):

            #Evaluate sum and make sure entry indices are not the same
            if entries[x]+entries[y]+entries[z] == 2020 and x != y and x !=z  and y != z:
                num1 = entries[x]
                num2 = entries[y]
                num3 = entries[z]
                product = entries[x]*entries[y]*entries[z]
                break

#Output results
print("Number 1: {}".format(num1))
print("Number 2: {}".format(num2))
print("Number 3: {}".format(num3))
print("Product: {}".format(product))
