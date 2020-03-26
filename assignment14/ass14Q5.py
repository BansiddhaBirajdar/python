'''5. Accept number from user and display below pattern.
Input : 8
Output : 2 4 6 8 10 12 14 16'''
def main():
    ino=int(input("Enter the ino :: "))
    if(ino<0):
        ino=-ino
    for i in range(2,ino+1):
        if(i%2==0):
            print(i,end=" ")

if __name__ == '__main__':
    main()