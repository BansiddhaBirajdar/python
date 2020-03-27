'''
4. Accept N numbers from user and display all such numbers which contains
3 digits in it.
Input : N : 6
Elements : 8225 665 3 76 953 858
Output : 665 953 858
'''
def diff(l):
    for i in range(len(l)):
        ch=str(l[i])
        if(len(ch)==3):
            print(ch,end=" ")

def main():
    ino=int(input("Enter the how you wanna insert :: "))
    l=[]
    for i in range(ino):
         a=int(input(f"enter the l[{i+1}]:: "))
         l.append(a)
    diff(l)
    
if __name__ == '__main__':
    main()