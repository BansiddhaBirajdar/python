'''2. Accept number from user and display below pattern.
Input : 5
Output : 5 # 4 # 3 # 2 # 1 #'''
def main():
    ino=int(input("Enter the ino :: "))
    if(ino<0):
        ino=-ino
    for i in range(ino,0,-1):
        print(i,end=" # ")

if __name__ == '__main__':
    main()
    