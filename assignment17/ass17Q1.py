'''
1. Accept number of rows and number of columns from user and display
below pattern.
Input : iRow = 4 iCol = 4
Output : 
1 2 3 4
5 6 7 8
9 1 2 3
4 5 6 7'''

def dis(irow,icol):
    a=1
    for i in range(1,irow+1):
        for j in range(1,icol+1):
            if(a==10):
                a=1
            print(a,end=" ")
            a+=1
        print("")
def main():
    ino1=int(input("Enter the irow ::"))
    ino2=int(input("Enter the icol ::"))
    if(ino1<0):
        ino1=-ino1
    if(ino2<0):
        ino2=-ino2
    dis(ino1,ino2)
if __name__ == '__main__':
    main()