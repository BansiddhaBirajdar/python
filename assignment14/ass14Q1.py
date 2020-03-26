'''1. Accept number from user and display below pattern.
Input : 5
Output : A B C D E'''
def Dis(ino):
    if(ino<0):
        ino=-ino
    a='A'
    while(ino>0):
        print(a,end=" ")
        ino-=1
        i=ord(a[0])
        i+=1
        a=chr(i)

def main():
    ino=int(input("Enter the ino ::"))
    Dis(ino)
if __name__ == '__main__':
    main()
    