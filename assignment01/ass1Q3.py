#3. Program to print 5 to 1 numbers on screen.
def main():
    ino=int(input("Enter the how many time you print::"));
    i=ino
    while(i>0):
        print(i,end=" ")
        i-=1
if __name__=='__main__':
    main()