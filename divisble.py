#Write a Python program that prompts the user to enter a number, x, and displays all numbers from 1 to x that are divisible by both 3 and 5.
x=int(input("please enter any integer number"))    
if x<0:
    for i in range(-3,x,-1):
        if i%3==0 or i%5==0:
            print(i)
elif x>0:
    for i in range(1,x+1):
        if i%3==0 or i%5==0:
            print(i)

   
   