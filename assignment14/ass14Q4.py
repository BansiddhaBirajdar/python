'''4. Accept number from user and display below pattern.
Input : 4
Output : # 1 * # 2 * # 3 * # 4 *'''
def main():
    ino=int(input("Enter the ino :: "))
    if(ino<0):
        ino=-ino
    for i in range(1,ino+1):
        print("# ",i,end=" * ")

if __name__ == '__main__':
    main()