'''
2. Write a program which accept width & height of rectangle from user and calculate
its area. (Area = Width * Height)
Input : 5.3 9.78
Output : 51.834
'''
def main():
    W=float(input("Enter the Width  :: "))
    H=float(input("Enter the Height :: "))
    print(f"calculate area is {round(W*H,3)}")

if __name__ == '__main__':
    main()
    