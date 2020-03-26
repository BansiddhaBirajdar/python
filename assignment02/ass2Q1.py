def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
def main():
    ino1=int(input("Enter the ino1 :: "))
    ino2=int(input("Enter the ino2 :: "))
    ino3=int(input("Enter the ino3 :: "))
    print(f"Sum of {add(ino1,ino2,ino3)}")
if __name__ == '__main__':
    main()
    