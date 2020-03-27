'''
5. Accept N numbers from user and accept one another number as NO ,
return frequency of NO form it.
Input : N : 6
NO: 66
Elements : 85 66 3 66 93 88
Output : 2
Input : N : 6
NO: 12
Elements : 85 11 3 15 11 111
Output : 0'''

def diff(l,no):
    count=0
    for i in range(len(l)):
        if(l[i]==no):
            count+=1
    return count
def main():
    ino=int(input("Enter the how you wanna insert :: "))
    l=[]
    for i in range(ino):
         a=int(input(f"enter the l[{i+1}]:: "))
         l.append(a)
    no=int(input("Enter the no you wanna check :: "))
    ans=diff(l,no)
    print(f"frequency of {no} numbers {ans}")
if __name__ == '__main__':
    main()