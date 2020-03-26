'''
3.Write a program to find even factorial of given number.
Input : 5
Output : 8 (4 * 2)
Input : -5
Output : 8 (4 * 2)
Input : 10
Output : 3840 (10 * 8 * 6 * 4 * 2)
'''

def fact(ino):
    if ino<0:
        ino=-ino
    if(ino==0):
        print("Enter the +ve number ")
        return
    else:
        mul=1
        for i in range(ino,0,-1):
                if(i%2==0):
                    mul*=i
        print(f"factorial of given number {ino} is {mul}")

def main():
    ino=int(input("Enter the ino ::"))
    fact(ino)
if __name__ == '__main__':
    main()