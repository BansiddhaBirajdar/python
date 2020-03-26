#4. Accept one number and check whether is is divisible by 5 or not.
def main():
    ino=int(input("Enter the no::"))
    if(ino==0):
        print("Enter the +ve no")
        return
    else:
        if(ino%5==0):
            print("it is divisible")
        else:
            print("it is not divisible")

if __name__=='__main__':
    main()