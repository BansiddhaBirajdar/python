'''2.Write a program which accept number from user and check whether it contains 0
in it or not.
Input : 2395
Output : There is no Zero
Input : 1018
Output : It Contains Zero
Input : 9000
Output : It Contains Zero'''

def Num(ino):
    #using string   
    no=str(ino)
    if(no.count('0')):
        print("zero is present")
    else:
        print("zero is not present")
    ino=int(ino)
    rev=0
    while(ino!=0):
        if(ino%10==0):
            rev=1
        ino=ino//10
    
    if(rev):
        print("zero is present")
    else:
        print("zero is not present")
def main():
    ino=int(input("Enter the no :: "));
    Num(ino)
if __name__ == '__main__':
    main()
    