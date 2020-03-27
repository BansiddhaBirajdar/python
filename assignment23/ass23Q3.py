'''
3. Accept N numbers from user and accept one another number as NO ,
return index of last occurrence of that NO.
Input : N : 6
NO: 66
Elements : 85 66 3 66 93 88
Output : 3
Input : N : 6
NO: 93
Elements : 85 66 3 66 93 88
Output : 4
Input : N : 6
NO: 12
Elements : 85 11 3 15 11 111
Output : -1
'''
def diff(l,no):
    p=-1
    for pos,i in enumerate(l):
        if(i==no):
            p=pos
    if(pos==-1):
        return p
    else:
        return p
def main():
    ino=int(input("Enter the how you wanna insert :: "))
    l=[]
    for i in range(ino):
         a=int(input(f"enter the l[{i+1}]:: "))
         l.append(a)
    no=int(input("Enter the no you wanna check :: "))
    ans=diff(l,no)
    if(ans==-1):
        print(f" {no} numbers  is index :: {ans}")
    else:
        print(f" {no} numbers  is index :: {ans}")
if __name__ == '__main__':
    main()