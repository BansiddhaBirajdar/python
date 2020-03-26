'''Write a program which accept number from user and display its multiplication of
factors.
Input : 12
Output : 144 (1 * 2 * 3 * 4 * 6)
Input : 13
Output : 1 (1)
Input : 10
Output : 10 (1 * 2 * 5)'''
def fact(ino):
    imult=1
    if(ino<0):
        ino=-ino
    if(ino==0):
        return 0
    i=1
    while(i<ino):
        if(ino%i==0):
            imult*=i
        i+=1
    return imult
def main():
    print("+++++++++++++FACTORS +++++++++++++++++")
    ino=int(input("Enter the no::"))
    ans=fact(ino)
    print(f"Output::{ans}")
if __name__=='__main__':
    main()