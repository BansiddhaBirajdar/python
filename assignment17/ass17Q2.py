'''2. Accept number of rows and number of columns from user and display
below pattern.
Input : iRow = 4 iCol = 4
Output : 
2 4 6 8 10
1 3 5 7 9
2 4 6 8 10
1 3 5 7 9'''

def dis(irow,icol):
    
    for i in range(1,irow+1):
        a=1
        b=2
        for j in range(1,icol+1):
            if(i%2!=0):
                print(b,end=" ")
                b+=2
            else:
                print(a,end=" ")
                a+=2
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