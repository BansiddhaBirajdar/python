'''Write a program which accept total marks & obtained marks from user and
calculate percentage.
Input : 1000 745
Output : 74.5%'''
def main():
    print("+++++++++++++++++ program +++++++++++++++++++")
    total=int(input("Enter the total marks::"))
    obt_m=int(input("Enter the obtained marks::"))
    if(total==0):
        print("Give a propar input")
        return
    if(obt_m ==0):
        print("Give a propar input")
        return
    ans=(obt_m/total)*100
    print(f"OUTPUT::{ans}%")
if __name__ == '__main__':
    main()
    