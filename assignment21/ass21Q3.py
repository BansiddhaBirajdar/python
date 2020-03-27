'''
3. Accept N numbers from user and display all such elements which are
even and divisible by 5.
Input : N : 6
Elements : 85 66 3 80 93 88
Output : 80'''
def diff(l):
    l1=[]
    for i in range(len(l)):
        if(l[i]%5==0 and l[i]%2==0):
            l1.append(l[i])
    return(l1)
def main():
    ino=int(input("Enter the how you wanna insert :: "))
    l=[]
    for i in range(ino):
         a=int(input(f"enter the l[{i+1}]:: "))
         l.append(a)
    ans=diff(l)
    print(f"Summation of even elements and summation of odd elements differences {ans}")
if __name__ == '__main__':
    main()