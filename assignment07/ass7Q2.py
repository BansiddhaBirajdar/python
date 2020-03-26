'''
2.Write a program which accept number from user and print numbers till that
number.
Input : 8
Output : 1 2 3 4 5 6 7 8'''
def dis(ino):
    if ino<0:
        ino=-ino
    if(ino==0):
        print("Enter the +ve number ")
        return
    else:
        for i in range(1,ino+1):
            print(i,end=" ")

def main():
    ino=int(input("Enter the ino ::"))
    dis(ino)
if __name__ == '__main__':
    main()
