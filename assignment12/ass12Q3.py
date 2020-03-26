'''3.Write a program which accept number from user and count frequency of 2 in it.
Input : 2395
Output : 1
Input : 1018
Output : 0
Input : 9000
Output : 0
Input : 922432
Output : 3'''

def Num(ino):
    #using string   
    no=str(ino)
    print(f"Output:: {no.count('2')}")
    ino=int(ino)
    rev=0
    while(ino!=0):
        if(ino%10==2):
            rev+=1
        ino=ino//10
    print("Output::",rev)
def main():
    ino=int(input("Enter the no :: "));
    Num(ino)
if __name__ == '__main__':
    main()
    