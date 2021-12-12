# My Solution for bonus task 1
# Wrote By Orel Rahum

##################################################################################################
# 1 . Write a python program to swap two numbers using a third variable
def task1():
    first_number = 100
    second_number = 200
    print("Before swap :")
    print(f"first value is :{first_number}, second value is :{second_number}\n")

    swap_helper = first_number
    first_number = second_number
    second_number = swap_helper

    print("After swap :")
    print(f"first value is :{first_number}, second value is :{second_number}")


##################################################################################################
# 2 . Write a python program to swap two numbers without using third variable
# help : https://www.javatpoint.com/program-to-swap-two-numbers-without-using-the-third-variable
def task2():
    first_number = 50
    second_number = 100
    print("Before swap :")
    print(f"first value is :{first_number}, second value is :{second_number}\n")

    first_number = first_number + second_number
    second_number = first_number - second_number
    first_number = first_number - second_number

    print("After swap :")
    print(f"first value is :{first_number}, second value is :{second_number}")


##################################################################################################
# 3 . Write a python program to read two numbers and find the sum of their cubes
def task3():
    first_number = input_number("Please enter your first number :")
    second_number = input_number("Please enter your second number :")

    first_number_cubes = first_number * first_number * first_number
    second_number_cubes = second_number * second_number * second_number

    print(f"your first input cubes is : {first_number}^3 = {first_number_cubes} ")
    print(f"your second input cubes is : {second_number}^3 = {second_number_cubes} ")
    print(f"the sum of both numbers is {first_number_cubes + second_number_cubes}")


##################################################################################################
# 4 . Write a python program to read three numbers and if any two variables are equal , print that number
def task4():
    first_number = input_number("Please enter your first number :")
    second_number = input_number("Please enter your second number :")
    third_number = input_number("Please enter your third number :")

    if first_number == second_number:
        print(f"the variables that equal is the first Number and second Number and they equal to :{first_number}")

    elif first_number == third_number:
        print(f"the variables that equal is the first Number and third number and they equal to :{first_number}")

    elif second_number == third_number:
        print(f"the variables that equal is the second number and third number and they equal to :{second_number}")
    else:
        print("no the 2 inputs that equal ")


##################################################################################################
# 5 . Write a python program to read three numbers and find the smallest among them
def task5():
    first_number = input_number("Please enter your first number : ")
    second_number = input_number("Please enter your second number :")
    third_number = input_number("Please enter your third number :")

    if first_number < second_number and first_number < third_number:
        print(f"The smallest variable is first number that equal to {first_number}")

    elif second_number < third_number:
        print(f"The smallest variable is second number that equal to {second_number}")

    else:
        print(f"The smallest variable is third number that equal to {third_number}")


##################################################################################################
# helper function

def input_number(text):
    number = input(text)
    while not number.isnumeric():
        number = input("Invalid input , " + text)

    return int(number)


##################################################################################################
# main

if __name__ == "__main__":
    task = input_number("Please choose your task number (from 1 to 5) :")
    print("")
    if task == 1:
        task1()
    elif task == 2:
        task2()
    elif task == 3:
        task3()
    elif task == 4:
        task4()
    elif task == 5:
        task5()
