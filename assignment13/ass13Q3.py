'''3.Write a program which accept number from user and return the count of digits in
between 3 and 7.
Input : 2395
Output : 1
Input : 1018
Output : 0
Input : 4521'''

def Num(ino):
    if(ino==0):
        return 0
    if(ino<0):
        ino=-ino
    a=0
    while(ino!=0):
        if((ino%10)>=3 and (ino%10)<=7):
            a+=1
        ino=ino//10
    print("output::",a)
def main():
    ino=int(input("Enter the no :: "));
    Num(ino)
if __name__ == '__main__':
    main()