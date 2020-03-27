'''1. Accept N numbers from user and return difference between summation
of even elements and summation of odd elements.
Input : N : 6
Elements : 85 66 3 80 93 88
Output : 53 (234 - 181)'''
def diff(l):
    even=0
    odd=0
    for i in range(len(l)):
        if(l[i]%2==0):
            even+=l[i]
        else:
            odd+=l[i]
    return(even-odd)
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