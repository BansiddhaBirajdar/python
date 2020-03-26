'''4.Write a program which accept number from user and return summation of all its
non factors.
Input : 12
Output : 50
Input : 10
Output : 37'''
def nonFactSum(ino):
    isum=0
    if(ino<0):
        ino=-ino
    if(ino==0):
        print("Enter a +ve number")
        return
    i=2;
    while(i<ino):
        if(ino%i!=0):
            isum+=i
        i+=1
    return isum
def main():
    print("+++++++++++++FACTORS +++++++++++++++++")
    ino=int(input("Enter the no::"))
    isum=nonFactSum(ino)
    print(f"Summation of non factors::{isum}")
if __name__=='__main__':
    main()
