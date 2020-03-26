#5. Accept one number from user and print that number of * on screen.
def main():
    ino=int(input("Enter the how many time you print::"));
    i=0
    while(i<ino):
        print(" * ",end="")
        i+=1
if __name__=='__main__':
    main()