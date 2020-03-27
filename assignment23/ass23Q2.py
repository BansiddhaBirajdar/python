'''2. Accept N numbers from user and accept one another number as NO ,
return index of first occurrence of that NO.
Input : N : 6
NO: 66
Elements : 85 66 3 66 93 88
Output : 1'''

def diff(l,no):
    for pos,i in enumerate(l):
        if(i==no):
            return pos
    return -1
def main():
    ino=int(input("Enter the how you wanna insert :: "))
    l=[]
    for i in range(ino):
         a=int(input(f"enter the l[{i+1}]:: "))
         l.append(a)
    no=int(input("Enter the no you wanna check :: "))
    ans=diff(l,no)
    if(ans==-1):
        print("numbers is not present")
    else:
        print(f" {no} numbers  is index :: {ans}")
if __name__ == '__main__':
    main()