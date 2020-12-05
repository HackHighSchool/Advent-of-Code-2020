list1=[]
list2=[]
c=0     #constant used to keep track of no. of lines of data in each passport
with open('file4.txt','r') as reader:
    for eachline in reader:
        string=str(eachline)
        if string=='\n':
            for i in range(c-1):
                list2[0]=list2[0]+' '+list2[1]
                list2.pop(1)
            list1.append(list2[0])
            list2=[]
            c=0
        else:
            string=string.strip('\n')
            list2.append(string)
            c+=1
vld_count=1
for i in list1:
    Dict = dict((x.strip(), y.strip())
                for x, y in (element.split(':')
                for element in i.split(' ')))
    f= Dict.keys()>={'byr','iyr','eyr','hgt','hcl','ecl','pid'}   #checks whether all these keys are present in the Dictionary(info in passport)
    if f==True:
        vld_count+=1
print(vld_count)

