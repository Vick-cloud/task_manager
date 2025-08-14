
# # # # # #Ask user to enter first name
# # # # # #first_name = input("first_name")
# # # # # #Ask user to enter last name
# # # # # #last_name = input("last_name")
# # # # # #print user's fullname in Uppercase
# # # # # #full_name= (f"{first_name} {last_name}")
# # # # # #print (full_name.upper())

# # # # # #age = input ("How old are you?\n")
# # # # # #if 18 <= int(age) and int(age) <= 45:
# # # # #   #  print("You can have access.")
# # # # # #else:
# # # # #  #   print("You are not allowed here.")



# # # # # #Ask user to input an integer
# # # # # #user = input ("input integer\n")
# # # # # #Find the integer modulo 2
# # # # # #if int(user) % 6 == 0:
# # # # #  #   print("even")
# # # # # #If modulo is equal to 0 print Even
# # # # # #else:
# # # # #  #   print("odd")
# # # # # # #Else print Odd



# # # # # # #Ask user to input their score as a number
# # # # # # score = float(input("input your score:"))
# # # # # # #If score is between 90 to 100 (inclusive) print grade A
# # # # # # if int(score) >=90 and int(score)<= 100:
# # # # # #     print ("grade A")
# # # # # # #If score is between 80 to 89 (inclusive) print grade B
# # # # # # if int(score) >=80 and int(score)<= 89:
# # # # # #     print ("grade B")
# # # # # # #If score is between 70 to 79 (inclusive) print grade C
# # # # # # if int(score) >=70 and int(score)<= 79:
# # # # # #     print ("grade C")
# # # # # # # if score is between 60 to 69 (inclusive) print grade D
# # # # # # if int(score) >=60 and int(score)<= 69:
# # # # # #     print ("grade D")
# # # # # # #If score is between 0 to 59 (inclusive) print grade F
# # # # # # if  int(score) >=0 and int(score)<= 59:
# # # # # #     print ("grade F")

# # # # # #Ask user to input their purchase amount as float
# # # # # purchase_amount = float(input("how much did you buy? \n"))

# # # # # #If the purchase is 100 cedis or more apply 20% discount and print the amount to pay
# # # # # if purchase_amount >= 100:
# # # # #     discount = 0.2 * purchase_amount
# # # # #     amount_to_pay = purchase_amount - discount
# # # # #     print (f"You have to pay: {amount_to_pay}")

# # # # #     #If the purchase is 50 cedis or more apply 10% discount and print amount to pay
# # # # # elif purchase_amount >= 50:
# # # # #     discount = 0.1 * purchase_amount
# # # # #     amount_to_pay = purchase_amount - discount
# # # # #     print (f"You have to pay: {amount_to_pay}")

# # # # #     # if the purchase is less than 50 cedis apply no discount and print amount to pay
# # # # # else:
# # # # #     print(f"You have to pay: {purchase_amount}")


# # # # # Ask user to input the length of the 3 sides of a triangle
# # # # # x = float(input("Enter the first side:"))
# # # # # y = float(input("Enter the second side:"))
# # # # # z = float(input("Enter the third side:"))

# # # # # If all sides are equal print Equaliateral 
# # # # # if x == y and y == z:
# # # # #     print  (f"You have an Equilateral")
# # # # # # If 2 sides are equal print isosceles
# # # # # elif x == y or y == z or x == z:
# # # # #     print (f"You have an Isosceles") 
# # # # # # If no sides are equal print scalene
# # # # # else: 
# # # # #     print (f"You have a Scalene")


# # # # file = open("tasks.txt", "r")
# # # # tasks = file.read().split("\n")
# # # # for task in tasks:
# # # #  print(f"{tasks.index(task)}. {task}")


# # # #use loop to calculate the sum of the numbers below

# # # # for x in numbers:
# # # #     print(x)

# # # numbers = [10, 5, 20, 8, 15]
# # # total_sum = 0 

# # # for number in numbers:
# # #         total_sum += number
# # # print("Sum of the numbers:", total_sum)


                  


# # #open the file emails.txt in Read mode
# # file = open("emails.txt", "r")
# # emails = file.read().split("\n")
# # for email in emails:
# #     username = email.split('@')[0]
# #     print(f"generated username:", username)
# # #Read and splut the data using \n to get a list
# # #Loop over the list of emails and print a generated username for each of them
# # # i.e username is all characters before the @


# def register_user(name, email, password):
#     #check if user does not already exist
#     # Hash user password
#     # validate inputs
#     # check if user is not a robot
#     # Return response
#     return "User registered successfully!"
# register_user("Michael Hammond", "mickymond@yahoo.com", "123456")


import add
import show
import update
import delete

add_task_response = add.task("sleep")
print(add_task_response)

show_task_response = show.show_tasks()
print(show_tasks_response)

update_task_response = update.update_tasks("sleep","wake up")
print(add_task_response)

delete_task_response = delete.delete_task("wake up")
print(delete_task_response)








