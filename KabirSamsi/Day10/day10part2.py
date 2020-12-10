from day10tree import Node

with open("day10jolts.txt", 'r') as file:
    lines = list(file.readlines())

jolts = [0] #Stores each joltage level, but contains 0 (the joltage of the node at the start of the chain)

#Strip and parse lines, then add them to the jolts
for line in lines:
    line = int(line.strip('\n'))
    jolts.append(line)

#Sort jolts and add the adaptor rating
jolts.sort()
jolts.append(jolts[len(jolts) - 1] + 3)


print("Waiting...")
head = Node(0, jolts, None) #Recursively creates a tree structure that stores each sequence as connected nodes

print(f"Total Sequences: {head.sequence_count}") #Output result (the number of sequences, starting with the head node)
