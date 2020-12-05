import math #Math module will be used for rounding operations

file = open("trees.txt", 'r')
fileArr = [] #File array contains each line from file (so file doesn't have to be reopended and reread each time)
slope = [] #Slope matrix stores info about the trees and open spots on the 'slope'

for line in file: #Add values from file to file array
    fileArr.append(line)

file.close()
line_count = len(fileArr) #Number of lines in the file

#For every line in the file, add 3 of the line to the file
for line in fileArr:
    slope.append(line[0:len(line)-1] * (len(line) * (math.ceil(line_count / len(line)) * 3)))

tree_count = 0 #Store how many trees are there
row = 0
col = 0

while (row < len(slope) - 1):
    #Move 3 to the right and 1 down
    row += 1
    col += 3

    #At every iteration, increment by 3 for columns and 1 for rows
    if slope[row][col] == '#':
        tree_count += 1

print("Tree Count: {}".format(tree_count)) #Output final result
