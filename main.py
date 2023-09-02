# import pygame 

# # ----- part 1 -------
# my_name = input("what is your name?")
# my_age = input("What is your age?")
# print(f"my name is {my_name} and I am {my_age} years old")

# # ------ part 2 -------

# first_namber = int(input("insert first number : "))
# secound_number = int(input("insert secound number : "))
# operation = input("insert the opertaion (* + - / ) : ")

# if operation == "+": 
#     print(f"{first_namber} {operation} {secound_number} =  {first_namber +secound_number}")
# elif operation == "-":
#     print(f"{first_namber} {operation} {secound_number} = {first_namber - secound_number}")
# elif operation == "*":
#     print(f"{first_namber} {operation} {secound_number} = {first_namber * secound_number}")
# elif operation == "/":
#     print(f"{first_namber} {operation} {secound_number} = {first_namber / secound_number}")
# else:
#     print("the opration is not valid")

# # ------- part 3 ---------

# bus_capacity = 50
# people_inside = int(input("how many passanger inside the bus :"))
# people_outside = int(input ("how many people want to ride the bus : "))
# empty_seats = bus_capacity - people_inside

# if empty_seats > people_outside : 
#     print(f"there are {empty_seats} empty seats avalible in the bus")
# else : 
#     print(" THE BUS IS FULL !! ")

user_regested = True
rightpassword = input("put the password : ")
if user_regested == False : 
    NewUsername = input("choose your username : ")
    rightpassword = rightpassword
else : 
    username = input ("Enter your username : ")
    password = input ("Eneter your password: ")
    while password != rightpassword: 
     password = input ("the pass is wrong Eneter your password: ")
    else: 
     print(f"welcom {username}")
     exit()