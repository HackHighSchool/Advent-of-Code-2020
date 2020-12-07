list1=[]
c=0  #counts the number of questions to which everyone answered "yes"
with open('file6.txt','r') as reader:
    for eachline in reader:
        list2=[]
        string=str(eachline)
        if string=='\n':   #checks if line is blank
            list1 = list(set.intersection(*map(set, list1))) # Takes intersecting answers from among the group and assigns it to list1
            c+=len(list1)
            list1=[]   #list is empty for the next group
        else:
            string=string.strip('\n') #remvoves the trailing '\n'
            for question in string:
                list2.append(question)  # list contains the questions with the answer "yes" of an individual person
                list1.append(list2)   #contains the answers of the whole group  
print('The number of questions to which everyone answered "yes"-->',c)
        
