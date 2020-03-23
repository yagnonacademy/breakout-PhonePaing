## Demonstrations for Chapter 7 - Iteration

import random

#function to add all the elements of a list
def add_em_up(mylist):
    sum=0
    for i in mylist:
        sum=sum+i
    return sum


BANK=0





def main():
    #a=[2,5,7,8,9]
    #print(add_em_up(a))
    rollagain="y"
    print(BANK)
    while True:
         s=random.randint(1,6)
         print(s)
         rollagain=input("Roll again?  y or n ")
         while (rollagain != "y") and (rollagain != "n") :
             rollagain=input("Roll again?  y or n ")
             

         if (rollagain != "y"):
             break
            



if __name__=="__main__":
    main()
