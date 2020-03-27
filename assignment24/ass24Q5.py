''' Accept N numbers from user and display summation of digits of each
number.
Input : N : 6
Elements : 8225 665 3 76 953 858
Output : 17 17 3 13 17 21
'''
def diff(l):
    
    for i in range(len(l)):
        sum=0
        while(l[i]!=0):
            sum+=(l[i]%10)
            l[i]=l[i]//10
        print(sum,end=" ")
def main():
    ino=int(input("Enter the how you wanna insert :: "))
    l=[]
    for i in range(ino):
         a=int(input(f"enter the l[{i+1}]:: "))
         l.append(a)
    diff(l)
if __name__ == '__main__':
    main()