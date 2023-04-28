from datetime import datetime 
mydob = (input("enter DOB(dd-mm-yyy):").split("-"))

mydobnew = []

for i in mydob:
    mydobnew.append(int(i))

    mydob = mydobnew
#validate someone born tommorow
    if len(mydob) !=3 or mydob[0]> 31 or mydob[o]<1\
    or mydob[1] < 1  or mydob[1] > 12 or mydob[2]>2023\
    or len(str(mydob[2])) !=4 or (mydob[1]== 2 and mydob[0]>29)\
    or(mydob[1]==2 and mydob[0]>28 and mydob[2] % 4 !=0)\
    or(mydob[1]%2==0 and mydob[0]>30 and mydob[1]<8)\
    or(mydob[1]%2!=0 and mydob[0]>30 and mydob [1]>7):
        
        
        print("invalid date")
    else:
        print(mydob)    