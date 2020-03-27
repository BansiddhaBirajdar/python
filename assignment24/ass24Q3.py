'''3. Accept N numbers from user and return the difference between largest
and smallest number.
Input : N : 6
Elements : 85 66 3 66 93 88
Output : 90 (93 -3)'''
def diff(l):
    return max(l)-min(l)
def main():
    ino=int(input("Enter the how you wanna insert :: "))
    l=[]
    for i in range(ino):
         a=int(input(f"enter the l[{i+1}]:: "))
         l.append(a)
    ans=diff(l)
    print(f"differnce Max and min :: {ans}")
if __name__ == '__main__':
    main()