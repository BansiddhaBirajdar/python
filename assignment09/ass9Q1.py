'''1.Write a program which accept number from user and display below pattern.
Input : 5
Output : * * * * * # # # # #
Input : 6
Output : * * * * * * # # # # # # #
Input : -5
Output : * * * * * # # # # #
Input : 2
Output : * * # #'''

def Dis(ino):
    if(ino==0):
        print("Enter the +ve number")
        return
    else:
        for i in range(ino+1):
            print("*",end=" ")
        for i in range(ino+1):
            print("#",end=" ")
def main():
    ino=int(input("Enter the no ::"))
    if (ino<0):
        ino=-ino
    Dis(ino)
if __name__ == '__main__':
    main()
    