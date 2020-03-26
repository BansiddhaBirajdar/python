'''1.Write a program which accept radius of circle from user and calculate its area.
Consider value of PI as 3.14. (Area = PI * Radius * Radius)
Input : 5.3
Output : 88.2026
Input : 10.4
Output : 339.6224'''
def area(ino):
    ino=float(ino)
    if(ino<0):
        print("Enter the +ve Radius")
        return
    PI=3.14
    return PI*ino*ino;

def main():
    R=input("Enter the Radius :: ")
    iret=area(R)
    print(f"Calculate area is {iret}")
if __name__ == '__main__':
    main()
    