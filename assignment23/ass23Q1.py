'''1. Accept N numbers from user and accept one another number as NO ,
check whether NO is present or not.
Input : N : 6
NO: 66
Elements : 85 66 3 66 93 88
Output : TRUE
Input : N : 6
NO: 12
Elements : 85 11 3 15 11 111
Output : FALSE'''

def diff(l,no):
    for i in range(len(l)):
        if(l[i]==no):
            return True
    return False
def main():
    ino=int(input("Enter the how you wanna insert :: "))
    l=[]
    for i in range(ino):
         a=int(input(f"enter the l[{i+1}]:: "))
         l.append(a)
    no=int(input("Enter the no you wanna check :: "))
    ans=diff(l,no)
    print(f" {no} numbers  is present :: {ans}")
if __name__ == '__main__':
    main()