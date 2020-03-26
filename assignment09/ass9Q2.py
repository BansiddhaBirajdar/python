'''
2. Accept amount in US dollar and return its corresponding value in Indian currency.
Consider 1$ as 70 rupees.
Input : 10
Output : 700
Input : 3
Output : 270
Input : 1200
Output : 84000
'''
def main():
    ino=int(input("Enter the indian Amount ::"))
    if(ino<0):
        ino=-ino
    if(ino==0):
        print("Enter the +ve Amount.")
        return
    print(f"US dollar is {ino*70}")
if __name__ == '__main__':
    main()
    