'''
5. Write a program which returns difference between Even factorial and odd factorial
of given number.
Input : 5
Output : -7 (8 - 15)
Input : -5
Output : -7 (8 - 15)
Input : 10
Output : 2895 (3840 - 945)
'''

def fact(ino):
    if ino<0:
        ino=-ino
    if(ino==0):
        print("Enter the +ve number ")
        return
    else:
        mul1=1
        mul2=1
        for i in range(ino,0,-1):
            if(i%2==0):
                mul1*=i
            else:
                mul2*=i
        print(f"factorial of given number {ino} is {mul1-mul2}")

def main():
    ino=int(input("Enter the ino ::"))
    fact(ino)
if __name__ == '__main__':
    main()