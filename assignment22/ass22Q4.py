'''
4. Accept N numbers from user and return frequency of 11 form it.
Input : N : 6
Elements : 85 66 3 15 93 88
Output : 0
Input : N : 6
Elements : 85 11 3 15 11 111
Output : 2'''

def diff(l):
    count=0
    for i in range(len(l)):
        if(l[i]==11):
            count+=1
    return count
def main():
    ino=int(input("Enter the how you wanna insert :: "))
    l=[]
    for i in range(ino):
         a=int(input(f"enter the l[{i+1}]:: "))
         l.append(a)
    ans=diff(l)
    print(f"11 present is {ans} time")
if __name__ == '__main__':
    main()