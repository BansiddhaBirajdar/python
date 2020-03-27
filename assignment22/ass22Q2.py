'''
2. Accept N numbers from user and return difference between frequency of
even number and odd numbers.
Input : N : 7
Elements : 85 66 3 80 93 88 90
Output : 1 (4 -3)'''

def diff(l):
    count_even=0
    count_odd=0
    for i in range(len(l)):
        if(l[i]%2==0):
            count_even+=1
        else:
            count_odd+=1
    return count_even-count_odd
def main():
    ino=int(input("Enter the how you wanna insert :: "))
    l=[]
    for i in range(ino):
         a=int(input(f"enter the l[{i+1}]:: "))
         l.append(a)
    ans=diff(l)
    print(f"frequency of even numbers and odd numbers {ans}")
if __name__ == '__main__':
    main()