'''
1. Accept number of rows and number of columns from user and display
below pattern.
Input : iRow = 4 iCol = 3
Output : 
* * *
* * *
* * *
* * *'''
def dis(ino):
    for i in range(ino):
        for j in range(ino):
            print("*",end=" ")
        print("")
def main():
    ino=int(input("Enter the ino ::"))
    if(ino<0):
        ino=-ino
    dis(ino)
if __name__ == '__main__':
    main()
