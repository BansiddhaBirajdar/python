'''Write a program which accept number from user and print its numbers line.
Input : 4
Output : -4 -3 -2 -1 0 1 2 3 4'''

def dis(ino):
    if ino<0:
        ino=-ino
    if(ino==0):
        print("Enter the +ve number ")
        return
    else:
        i=-ino
        while(i<=ino):
            print(i,end=" ")
            i+=1

def main():
    ino=int(input("Enter the ino ::"))
    dis(ino)
if __name__ == '__main__':
    main()
