'''3. Write a program which accept two numbers and check whether numbers are
equal or not.
Input : 10 10
Output : Equal
Input : 10 12
Output : Not Equal
Input : 10 -10
Output : Not Equal'''
def main():
    print("+++++++++++++++++++program3++++++++++++++++++++")
    ino1=int(input("Enter the ino1::"))
    ino2=int(input("Enter the ino2::"))
    if(ino1==ino2):
        print("output::Equal")
    else:
        print("output::Not Equal")
if __name__ == "__main__":
    main()