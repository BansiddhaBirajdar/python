'''
2. Accept N numbers from user and return the smallest number.
Input : N : 6
Elements : 85 66 3 66 93 88
Output : 3

'''
def diff(l):
    return min(l)
def main():
    ino=int(input("Enter the how you wanna insert :: "))
    l=[]
    for i in range(ino):
         a=int(input(f"enter the l[{i+1}]:: "))
         l.append(a)
    ans=diff(l)
    print(f"Min:: {ans}")
if __name__ == '__main__':
    main()