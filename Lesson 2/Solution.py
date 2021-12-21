# My Solution for assignment  1
# Wrote By Orel Rahum

##################################################################################################
# Part A
print("\n##########################################################################################")
print("                                      part A \n")
X = 7
Y = 44.3
# print results
if X > Y:
    print(f"BIG, X{X} is Bigger than Y{Y}")
if Y > X:
    print(f"small, X{X} is smaller than Y{Y}")

##################################################################################################
# Part B
print("\n##########################################################################################")
print("                                      part B \n")
for index in range(1, 6):
    print(f"Iteration number is {index} ")

##################################################################################################
# Part C
print("\n##########################################################################################")
print("                                      part C \n")

my_number = 1

if my_number == 1:
    print("summer")
if my_number == 2:
    print("winter")
if my_number == 3:
    print("fall")
if my_number == 4:
    print("spring")

##################################################################################################
# Part D
print("\n##########################################################################################")
print("                                      part D \n")

# It will run 10 times (from 1-10)

# count = 1
# while count < 11:
#    print(count)
#    count = count + 1

print("The code we get will print 10 in last loop")

##################################################################################################
# Part E
print("\n##########################################################################################")
print("                                      part E \n")

my_age = 26
first_letter_on_my_last_name = "O"
shekels_to_dollar = 0.32
dollar_to_shekels = 3.11
flew_abroad = True
apartment_number = 36
print(f"My Age is {my_age}\nThe first letter on my last name is {first_letter_on_my_last_name}")
print(f"Did me flew abroad? {flew_abroad}\nMy apartment number is {apartment_number}")
print(f"1 shekel is {shekels_to_dollar} dollar")
print(f"1 dollar is {dollar_to_shekels} shekel")
print(f"My age + the currenty is :{my_age + dollar_to_shekels}")

##################################################################################################
# Part F
print("\n##########################################################################################")
print("                                      part F \n")


def part_F():
    phone_number = input("Please enter your phone number : ")
    while not phone_number.isnumeric():
        phone_number = input("Invalid number, Please enter your phone number : ")
    print(f"Your Phone number is :{phone_number}")


##################################################################################################
# Part G
print("\n##########################################################################################")
print("                                      part G \n")


def printHello():
    print("hello")


def calculate():
    print(5 + 3.2)


##################################################################################################
# Part H
print("\n##########################################################################################")
print("                                      part H \n")


def input_name():
    name = input("Please Enter your name ")
    print(f"Your name is {name}")


def devide(x, y):
    if y == 0:
        print("impossible")
        return
    print(x / y)


##################################################################################################
# Part I
print("\n##########################################################################################")
print("                                      part I \n")


def sum(x, y):
    return x + y


def add_space(s1, s2):
    return s1 + " " + s2


##################################################################################################
# Part K
print("\n##########################################################################################")
print("                                      part K \n")

for index in range(5):
    for index2 in range(index + 1):
        print("#", end=" ")
    print("")

##################################################################################################
# Part L
print("\n##########################################################################################")
print("                                      part L \n")

number = 7
for index in range(number):
    for index2 in range(number):
        if index == index2 or (index + index2) == (number - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")

##################################################################################################
# Part M(1)
print("\n##########################################################################################")
print("                                      part M(1) \n")


def get_number():
    text = "please Enter your number"
    input_number = input(text)
    while not input_number.isnumeric():
        input_number = input("Invalid input , " + text)

    return int(input_number)


##################################################################################################
# Part M(2)
print("\n##########################################################################################")
print("                                      part M(2) \n")


def result(number):
    sum_digit = 0
    if number < 10:
        return number
    while number >= 1:
        sum_digit += number % 10
        number = int(number / 10)
    return sum_digit


result(27)
