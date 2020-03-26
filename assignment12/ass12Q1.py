'''1.Write a program which accept number from user and display its digits in reverse
order.
Input : 2395
Output : 5
9
3
2'''
def Num(ino):
    #using string   
    no=str(ino)
    print("REVERSE::",no[::-1])
    ino=int(ino)
    rev=0
    while(ino!=0):
        rev=rev*10+(ino%10)
        ino=ino//10
    print("\n Reverse::",rev)
def main():
    ino=int(input("Enter the no :: "));
    Num(ino)
if __name__ == '__main__':
    main()
    