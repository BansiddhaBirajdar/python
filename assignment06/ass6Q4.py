'''4. Write a program which accept three numbers and print its multiplication.
Input : 5 4 7
Output : 140
Input : 5 0 7
Output : 35
Input : 0 0 0
Output : 0'''
def main():
    print("+++++++++++++++++ program3 ++++++++++++++")
    ino1=int(input("Enter the no1::"))
    ino2=int(input("Enter the no2::"))
    ino3=int(input("Enter the no3::"))
    if(ino1==0 and ino2==0 and ino3==0):
        print(f"Output::{0}")
    elif(ino2==0 or ino3==0 or ino1==0):
        if(ino1==0):
            ino1=1
        if(ino2==0):
            ino2=1
        if(ino3==0):
            ino3=1
        print(f"Output::{ino1*ino2*ino3}")
    else:
        print(f"Output::{ino1*ino2*ino3}")

if __name__ == '__main__':
    main()
    