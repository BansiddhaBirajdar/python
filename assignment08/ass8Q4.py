'''4.Write a program which accept number from user and display its table.
Input : 2
Output : 2 4 6 8 10 12 14 16 18 20
Input : 5
Output : 5 10 15 20 25 30 35 40 45 50
Input : -5
Output : 5 10 15 20 25 30 35 40 45 50'''

def dis(ino):
    if ino<0:
        ino=-ino
    if(ino==0):
        print("Enter the +ve number ")
        return
    else:
        for i in range(1,11):
                print(ino*i,end=" ")

def main():
    ino=int(input("Enter the ino ::"))
    dis(ino)
if __name__ == '__main__':
    main()