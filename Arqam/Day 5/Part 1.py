import sys
with open('file5.txt','r') as reader: 
    List=[]
    for eachline in reader:
        List.append(str((eachline.strip('\n'))))
seat_id_max=0
seat_id_min=100    #Temp minimum seat id
List2=[]
for b_pass in List:
    x=127   #maximum no. of rows
    y=0     #minimum no. of rows
    a=7     #maximum no. of columns
    b=0     #minimum no. of columns
    for character in b_pass:
        if character=='F':
            diff=(x-y)//2
            if diff==0:
                x=y
            else:
                x=y+diff
        elif character=='B':
            diff=(x-y)//2
            if diff!=0:
                y=x-diff
        elif character=='L':
            diff=(a-b)//2
            if diff==0:
                a=b
            else:
                a=b+diff
        else:
            diff=(a-b)//2
            if diff!=0:
                b=a-diff
    seat_id=x*8+a
    if seat_id>seat_id_max:
        seat_id_max=seat_id
print('The maximum seat id is-->',seat_id_max)
    
    
    
            
