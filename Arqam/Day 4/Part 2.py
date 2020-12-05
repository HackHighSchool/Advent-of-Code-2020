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
d=0
for i in list1:
    Dict = dict((x.strip(), y.strip())
                for x, y in (element.split(':')
                for element in i.split(' ')))
    f= Dict.keys()>={'byr','iyr','eyr','hgt','hcl','ecl','pid'}  #checks whether all these keys are present in the Dictionary(info in passport)
    if f==True:
        if int(Dict['byr'])>=1920 and int(Dict['byr'])<=2002:
            if int(Dict['iyr'])>=2010 and int(Dict['iyr'])<=2020:
                if int(Dict['eyr'])>=2020 and int(Dict['eyr'])<=2030:
                    if Dict['ecl'] in ['amb','blu','gry','grn','hzl','oth','brn']:
                        if len(Dict['pid'])==9:
                            if Dict['hcl'][0]=='#' and len(Dict['hcl'])==7:
                                for character in range(1,7):
                                    if Dict['hcl'][character] in ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']:
                                        d+=1  #counts the number of valid characters 
                                if d==6:    # There must be 6 characters among 0-9 and a-f in hcl after the '#'.
                                    hgt=Dict['hgt']   
                                    unit=hgt[-2:]
                                    hgt=int(hgt[:-2])
                                    if unit=='cm'and hgt>=150 and hgt<=193:
                                        vld_count+=1
                                    elif unit=='in'and hgt>=59 and hgt<=76:
                                        vld_count+=1
                                d=0     #resets to 0 for the next passport
print('No.of Valid Passports-->',vld_count)




