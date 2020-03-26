'''3.Write a program to find factorial of given number.
Input : 5
Output : 120 (5 * 4 * 3 * 2 * 1)
Input : -5
Output : 120 (5 * 4 * 3 * 2 * 1)
Input : 4
Output : 24 (4 * 3 * 2 * 1)'''

def fact(ino):
    if ino<0:
        ino=-ino
    if(ino==0):
        print("Enter the +ve number ")
        return
    else:
        mul=1
        for i in range(ino,0,-1):
            mul*=i
        print(f"factorial of given number {ino} is {mul}")

def main():
    ino=int(input("Enter the ino ::"))
    fact(ino)
if __name__ == '__main__':
    main()