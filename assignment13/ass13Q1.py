'''1.Write a program which accept number from user and return the count of even
digits.
Input : 2395
Output : 1
Input : 1018
Output : 2
Input : -1018
Output : 2
Input : 8462
Output : 4'''
def Num(ino):
    if(ino==0):
        return 0
    if(ino<0):
        ino=-ino
    a=0
    while(ino!=0):
        if((ino%10)%2==0):
            a+=1
        ino=ino//10
    print("output::",a)
def main():
    ino=int(input("Enter the no :: "));
    Num(ino)
if __name__ == '__main__':
    main()