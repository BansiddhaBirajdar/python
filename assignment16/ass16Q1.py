'''
1. Accept number of rows and number of columns from user and display below
pattern.
Input : iRow = 4 iCol = 4
Output : 
A B C D
A B C D
A B C D
A B C D'''

def dis(irow,icol):
    for i in range(irow):
        a='A'
        for j in range(1,icol+1):
            print(a,end=" ")
            b=ord(a[0])
            b+=1
            a=chr(b)
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