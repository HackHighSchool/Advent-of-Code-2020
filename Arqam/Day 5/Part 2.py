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
    for each_character in b_pass:
        if each_character=='F':
            diff=(x-y)//2
            if diff==0:
                x=y
            else:
                x=y+diff
        elif each_character=='B':
            diff=(x-y)//2
            if diff!=0:
                y=x-diff
        elif each_character=='L':
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
    List2.append(seat_id)
    if seat_id>seat_id_max:
        seat_id_max=seat_id
    elif seat_id<seat_id_min:
        seat_id_min=seat_id
List2.sort()
for my_seat in range(len(List2)):
    if my_seat==len(List2)-1:
        sys.exit()
    if List2[my_seat]+2==List2[my_seat+1]:
        print('My seat is-->',List2[my_seat]+1)
        
        
    
