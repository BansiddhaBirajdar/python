'''!
2. Write a program which accept range from user and display all even numbers in
between that range.
Input : 23 35
Output : 24 26 28 30 32 34
Input : 10 18
Output : 10 12 14 16 18
Input : 10 10
Output : 10
Input : -10 2
Output : -10 -8 -6 -4 -2 0 2
Input : 90 18
Output : Invalid range'''

def Dis(ino1,ino2):
    if(ino1>ino2):
        print("Invalid range")
        return
    else:
        while(ino1<=ino2):
            if(ino1%2==0):
                print(ino1,end=" ")
            ino1+=1
def main():
    ino1=int(input("Enter the ino1::"))
    ino2=int(input("Enter the ino2::"))
    Dis(ino1,ino2)
if __name__ == '__main__':
    main()
    