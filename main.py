
# #Ask user to enter first name
# #first_name = input("first_name")
# #Ask user to enter last name
# #last_name = input("last_name")
# #print user's fullname in Uppercase
# #full_name= (f"{first_name} {last_name}")
# #print (full_name.upper())

# #age = input ("How old are you?\n")
# #if 18 <= int(age) and int(age) <= 45:
#   #  print("You can have access.")
# #else:
#  #   print("You are not allowed here.")



# #Ask user to input an integer
# #user = input ("input integer\n")
# #Find the integer modulo 2
# #if int(user) % 6 == 0:
#  #   print("even")
# #If modulo is equal to 0 print Even
# #else:
#  #   print("odd")
# # #Else print Odd



# # #Ask user to input their score as a number
# # score = float(input("input your score:"))
# # #If score is between 90 to 100 (inclusive) print grade A
# # if int(score) >=90 and int(score)<= 100:
# #     print ("grade A")
# # #If score is between 80 to 89 (inclusive) print grade B
# # if int(score) >=80 and int(score)<= 89:
# #     print ("grade B")
# # #If score is between 70 to 79 (inclusive) print grade C
# # if int(score) >=70 and int(score)<= 79:
# #     print ("grade C")
# # # if score is between 60 to 69 (inclusive) print grade D
# # if int(score) >=60 and int(score)<= 69:
# #     print ("grade D")
# # #If score is between 0 to 59 (inclusive) print grade F
# # if  int(score) >=0 and int(score)<= 59:
# #     print ("grade F")

# #Ask user to input their purchase amount as float
# purchase_amount = float(input("how much did you buy? \n"))

# #If the purchase is 100 cedis or more apply 20% discount and print the amount to pay
# if purchase_amount >= 100:
#     discount = 0.2 * purchase_amount
#     amount_to_pay = purchase_amount - discount
#     print (f"You have to pay: {amount_to_pay}")

#     #If the purchase is 50 cedis or more apply 10% discount and print amount to pay
# elif purchase_amount >= 50:
#     discount = 0.1 * purchase_amount
#     amount_to_pay = purchase_amount - discount
#     print (f"You have to pay: {amount_to_pay}")

#     # if the purchase is less than 50 cedis apply no discount and print amount to pay
# else:
#     print(f"You have to pay: {purchase_amount}")


# Ask user to input the length of the 3 sides of a triangle
x = float(input("Enter the first side:"))
y = float(input("Enter the second side:"))
z = float(input("Enter the third side:"))

# If all sides are equal print Equaliateral 
if x == y and y == z:
    print  (f"You have an Equilateral")
# If 2 sides are equal print isosceles
elif x == y or y == z or x == z:
    print (f"You have an Isosceles") 
# If no sides are equal print scalene
else: 
    print (f"You have a Scalene")






                  


