'''5. Write a program which accept N and print first 5 multiples of N.
Input : 4
Output : 4 8 12 16 20'''

def dis(ino):
    if ino<0:
        ino=-ino
    if(ino==0):
        print("Enter the +ve number ")
        return
    else:
        for i in range(1,6):
                print(ino*i,end=" ")

def main():
    ino=int(input("Enter the ino ::"))
    dis(ino)
if __name__ == '__main__':
    main()
