'''Accept number of rows and number of columns from user and display below
pattern.
Input : iRow = 3 iCol = 5
Output : 
A A A A A
B B B B B
C C C C C'''

def dis(irow,icol):
    a='A'
    for i in range(irow):
        for j in range(1,icol+1):
            print(a,end=" ")
        print("")
        b=ord(a[0])
        b+=1
        a=chr(b)
        
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