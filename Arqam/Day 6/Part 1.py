list1=[]
list2=[]
c=0   #constant to keep track of no. of people in a group
with open('file6.txt','r') as reader:
    for eachline in reader:
        string=str(eachline)
        if string=='\n':   #checks if line is blank
            for i in range(c-1):
                list2[0]=list2[0]+list2[1]  #adds all strings in the list to become one using a for loop.
                list2.pop(1)  #pops the added string and list2[2] takes place of list2[1]
            list1.append(list2[0])
            list2=[]
            c=0
        else:
            string=string.strip('\n') #remvoves the trailing '\n'
            list2.append(string)
            c+=1
x=0 # counts the number of questions to which anyone answered "yes"
for group in list1:
    list2=[]   #reassigning a new value to the old list
    for question in group:
        list2.append(question) #appends each character representing a question into a list
    list2=list(set(list2))  #set() removes duplicates from the list
    x+=len(list2)
print('The number of questions to which anyone answered "yes"-->',x)
        
