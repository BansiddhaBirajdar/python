'''5.Write a program which accept number from user and return difference between
summation of even digits and summation of odd digits.
Input : 2395
Output : -15 (2 - 17)
Input : 1018
Output : 6 (8 - 2)
Input : 8440
Output : 16 (16 - 0)
Input : 5733
Output : -18 (0 - 18)'''
def Num(ino):
    if(ino==0):
        return 0
    if(ino<0):
        ino=-ino
    a=0
    a1=0
    while(ino!=0):
        if((ino%10)%2==0):
            a=a+(ino%10)
        else:
            a1=a1+(ino%10)
        ino=ino//10
    print("output::",a-a1)
def main():
    ino=int(input("Enter the no :: "));
    Num(ino)
if __name__ == '__main__':
    main()