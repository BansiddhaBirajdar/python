'''5.Write a program which accept number from user and return difference between
summation of all its factors and non factors.
Input : 12
Output : -34 (16 - 50)
Input : 10
Output : -29 (8 - 37)'''
def factDiff(ino):
    isum1=isum2=0
    if(ino<0):
        ino=-ino
    if(ino==0):
        print("Enter a +ve number")
        return
    i=1;
    while(i<ino):
        if(ino%i!=0):
            isum2+=i
        else:
            isum1+=i
        i+=1
    return isum1-isum2
def main():
    print("+++++++++++++FACTORS +++++++++++++++++")
    ino=int(input("Enter the no::"))
    id=factDiff(ino)
    print(f"Differens factors::{id}")
if __name__=='__main__':
    main()
