'''4.Write a program which accept number from user and return multiplication of all
digits.
Input : 2395
Output : 270
Input : 1018
Output : 8
Input : 9440
Output : 144
Input : 922432
Output : 864'''
def Num(ino):
    if(ino==0):
        return 0
    if(ino<0):
        ino=-ino
    a=1
    while(ino!=0):
        i=(ino%10)
        if(ino%10==0):
            i=1
        a=a*i
        ino=ino//10
    print("output::",a)
def main():
    ino=int(input("Enter the no :: "));
    Num(ino)
if __name__ == '__main__':
    main()