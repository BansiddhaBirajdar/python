''' Write a program which accept one number from user and check whether that
number is greater than 100 or not.
Input : 101
Output : Greater
Input : 39
Output : Smaller'''
def checkNo(ino):
    if(ino==0 or ino<0):
        print("Please entered a +ve number")
        return
    else:
        if(ino>=100):
            return 'Greater'
        else:
            return 'Smaller'
def main():
    print("++++++++++++program2+++++++++++++++")
    ino=int(input("Enter the no::"))
    ans=checkNo(ino)
    if(ans=='Greater'):
        print(f"{ino} is  Greater")
    elif(ans=='Smaller'):
        print(f"{ino} is  Smaller")
    else:
        pass
if __name__=='__main__':
    main()