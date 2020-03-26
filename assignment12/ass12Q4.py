'''4.Write a program which accept number from user and count frequency of 4 in it.
Input : 2395
Output : 0
Input : 1018
Output : 0
Input : 9440
Output : 2
Input : 922432
Output : 1'''

def Num(ino):
    #using string   
    no=str(ino)
    print(f"Output:: {no.count('4')}")
    ino=int(ino)
    rev=0
    while(ino!=0):
        if(ino%10==4):
            rev+=1
        ino=ino//10
    print("Output::",rev)
def main():
    ino=int(input("Enter the no :: "));
    Num(ino)
if __name__ == '__main__':
    main()