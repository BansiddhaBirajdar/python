'''
4. Write a program which accepts N from user and print all odd numbers up to N.
Input : 18
Output : 1 3 5 7 9 11 13
'''
def dis(ino):
    if ino<0:
        ino=-ino
    if(ino==0):
        print("Enter the +ve number ")
        return
    else:
        for i in range(2,ino+1):
            if(i%2==0):
                print(i,end=" ")

def main():
    ino=int(input("Enter the ino ::"))
    dis(ino)
if __name__ == '__main__':
    main()
