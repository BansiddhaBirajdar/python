'''
4. Accept N numbers from user and accept Range, Display all elements from
that range
Input : N : 6
Start: 60
End : 90
Elements : 85 66 3 76 93 88
'''

def diff(l,str,end):
    for i in range(len(l)):
        if(l[i]>=str and l[i]<=end):
            print(f"{l[i]}")
def main():
    ino=int(input("Enter the how you wanna insert :: "))
    l=[]
    for i in range(ino):
         a=int(input(f"enter the l[{i+1}]:: "))
         l.append(a)
    str=int(input("Enter the str :: "))
    end=int(input("Enter the end :: "))
    diff(l,str,end)
if __name__ == '__main__':
    main()