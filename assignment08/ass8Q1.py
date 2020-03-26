'''
1. Write a program which accept number from user and if number is less than 50
then print small , if it is greater than 50 and less than 100 then print medium, if it is
greater than 100 then print large.
Input : 75
Output : Medium
'''
def Dis(ino):
    print("OUTPUT::")
    if (ino<=0):
        print("Enter the +ve number ")
        return
    else:
        if(ino<=50):
            print("small")
        elif(ino>50 and ino<=100):
            print("medium")
        else:
            print("large")
def main():
    ino=int(input("Enter the ino :: "))
    Dis(ino)
if __name__=="__main__":
    main()

