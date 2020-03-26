'''
3. Write a program which accept range from user and return addition of all numbers
in between that range. (Range should contains positive numbers only)
Input : 23 30
Output : 212
'''
def Dis(ino1,ino2):
    if(ino1>ino2 or ino1<0 or ino2<0):
        print("Invalid range")
        return
    else:
        add=0
        while(ino1<=ino2):
            add+=ino1
            ino1+=1
        return add
def main():
    ino1=int(input("Enter the ino1::"))
    ino2=int(input("Enter the ino2::"))
    print("addition is ::",Dis(ino1,ino2))
if __name__ == '__main__':
    main()
    