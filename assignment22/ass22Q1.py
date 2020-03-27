'''1. Accept N numbers from user and return frequency of even numbers.
Input : N : 6
Elements : 85 66 3 80 93 88
Output : 3'''
def diff(l):
    count=0
    for i in range(len(l)):
        if(l[i]%2==0):
            count+=1
    return count
def main():
    ino=int(input("Enter the how you wanna insert :: "))
    l=[]
    for i in range(ino):
         a=int(input(f"enter the l[{i+1}]:: "))
         l.append(a)
    ans=diff(l)
    print(f"frequency of even numbers {ans}")
if __name__ == '__main__':
    main()