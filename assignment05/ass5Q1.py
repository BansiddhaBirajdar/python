'''2.Write a program which accept number from user and display its factors in decreasing order.
Input : 12
Output : 6 4 3 2 1
Input : 13
Output : 1
Input : 10
Output : 5 2 1'''
def factDec(ino):
    imult=1
    print("Output::",end="")
    if(ino<0):
        ino=-ino
    if(ino==0):
        print("Enter a +ve number")
        return
    i=ino//2;
    while(i>0):
        if(ino%i==0):
            print( i,end=" ")
        i-=1
def main():
    print("+++++++++++++FACTORS +++++++++++++++++")
    ino=int(input("Enter the no::"))
    factDec(ino)
if __name__=='__main__':
    main()