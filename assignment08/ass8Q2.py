'''2. Accept single digit number from user and print it into word.
Input : 9
Output : Nine
Input : -3
Output : Three
Input : 12
Output : Invalid Number'''
def Dis(ino):
    no={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
    if(ino<0):
        ino=-ino
    else:
        print(f"OUTPUT::{no[ino]}")
def main():
    ino=int(input("Enter the  ino ::"))
    Dis(ino)
if __name__ == '__main__':
    main()
    