'''1.Write a program which accept number from user and print that number of $ & *
on screen.
Input : 5
Output : $ * $ * $ * $ * $ *
Input : 3
Output : $ * $ * $ *
Input : -3
Output : $ * $ * $ * 
'''
def dis(ino):
    if(ino<0):
        ino=-ino
    if(ino==0):
        print("Enter the +ve number ")
        return
    else:
        while (ino>0):
            print("$ * ",end=" ")
            ino-=1

def main():
    ino=int(input("Enter the +ve number :: "))
    dis(ino)
if __name__ == '__main__':
    main()
    