'''
5. Accept N numbers from user and return product of all odd elements.
Input : N : 6
Elements : 15 66 3 70 10 88
Output : 45
Input : N : 6
Elements : 44 66 72 70 10 88
Output : 0
'''
def diff(l):
    mul=1
    for i in range(len(l)):
        if(l[i]%2!=0):
            mul*=l[i]
    return mul
def main():
    ino=int(input("Enter the how you wanna insert :: "))
    l=[]
    for i in range(ino):
         a=int(input(f"enter the l[{i+1}]:: "))
         l.append(a)
    ans=diff(l)
    print(f"product of odd :: {ans}")
if __name__ == '__main__':
    main()