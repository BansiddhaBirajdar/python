'''5. Write a program which accept area in square feet and convert it into square
meter. (1 square feet = 0.0929 Square meter)
Input : 5
Output : 0.464515
Input : 7
Output : 0.650321'''
def main():
    ino=float(input("Enter the feet :: "))
    print(f"Squre meter{round(0.0929*ino,4)}")
if __name__ == '__main__':
    main()
    