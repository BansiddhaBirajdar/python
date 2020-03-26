'''3.Write a program which accept number from user and display all its non factors.
Input : 12
Output : 5 7 8 9 10 11
Input : 13
Output : 2 3 4 5 6 7 8 9 10 11 12
Input : 10
Output : 3 4 6 7 8 9'''
def factNon(ino):
    imult=1
    print("Output::",end="")
    if(ino<0):
        ino=-ino
    if(ino==0):
        print("Enter a +ve number")
        return
    i=2
    while(i<ino):
        if(ino%i!=0):
            print( i,end=" ")
        i+=1
def main():
    print("+++++++++++++NON FACTORS +++++++++++++++++")
    ino=int(input("Enter the no::"))
    factNon(ino)
if __name__=='__main__':
    main()