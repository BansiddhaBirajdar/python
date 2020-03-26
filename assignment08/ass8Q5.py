
def dis(ino):
    if ino<0:
        ino=-ino
    if(ino==0):
        print("Enter the +ve number ")
        return
    else:
        for i in range(10,0,-1):
                print(ino*i,end=" ")

def main():
    ino=int(input("Enter the ino ::"))
    dis(ino)
if __name__ == '__main__':
    main()