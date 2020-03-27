'''3. Accept N numbers from user check whether that numbers contains 11 in
it or not.
Input : N : 6
Elements : 85 66 11 80 93 88
Output : 11 is present
Input : N : 6
Elements : 85 66 3 80 93 88
Output : 11 is absent'''

def diff(l):
    count=0
    for i in range(len(l)):
        if(l[i]==11):
            count=1
    return count
def main():
    ino=int(input("Enter the how you wanna insert :: "))
    l=[]
    for i in range(ino):
         a=int(input(f"enter the l[{i+1}]:: "))
         l.append(a)
    ans=diff(l)
    if(ans):
        print(" 11 is present")
    else:
        print(" 11 is absent")
if __name__ == '__main__':
    main()