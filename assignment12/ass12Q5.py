'''5.Write a program which accept number from user and count frequency of such a
digits which are less than 6.
Input : 2395
Output : 3
Input : 1018
Output : 3
Input : 9440
Output : 3
Input : 96672
Output : 1'''
def Num(ino):
    #using string   
    no=str(ino)
    #print(f"Output:: {no.count('0','6')}")
    ino=int(ino)
    rev=0
    while(ino!=0):
        if(ino%10<6):
            rev+=1
        ino=ino//10
    print("Output::",rev)
def main():
    ino=int(input("Enter the no :: "));
    Num(ino)
if __name__ == '__main__':
    main()