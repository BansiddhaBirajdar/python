'''Program to divide two numbers'''

def main():
    ino1=int(input("Enter the no1::"))
    ino2=int(input("Enter the no2::"))
    if(ino2<=0):
        print("Please enter +ve no")
        return
    else:
        print("Division of ::",ino1//ino2);

if __name__ == "__main__":
    
    main()