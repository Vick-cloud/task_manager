# #program to calculate the average of two numbers\

#take two numbers as input
num1 = int(input("insert first number : "))
num2 = int(input("insert second number : "))
#declare the average variable
avg = (num1 + num2) /2
print (avg)

#Accept an input from the user and a full name
age = int(input("enter your age: "))
fullname = str(input("enter your fullname: "))

#If the age is less than 18 and the average is equal to 20, 

if age < 18 and int(avg) == 20:
#print {name}, you are not allowed to vote
print(f"")
#if the age is greater than or equal to 18 and the average is
#greater than or equal to 20, print {name}, you are allowed to vote
