# My Solution for bonus task 1
# Wrote By Orel Rahum

##################################################################################################
# 1 . Write a python program to swap two numbers using a third variable
def task1():
    first_number = 100
    second_number = 200
    print("Before swap :")
    print(f"the first value is:{first_number}, the second value is:{second_number}\n")

    swap_helper = first_number
    first_number = second_number
    second_number = swap_helper

    print("After swap :")
    print(f"the first value is:{first_number}, the second value is:{second_number}")


##################################################################################################
# 2 . Write a python program to swap two numbers without using third variable
# help : https://www.javatpoint.com/program-to-swap-two-numbers-without-using-the-third-variable
def task2():
    first_number = 50
    second_number = 100
    print("Before swap :")
    print(f"the first value is:{first_number}, the second value is:{second_number}\n")

    first_number = first_number + second_number
    second_number = first_number - second_number
    first_number = first_number - second_number

    print("After swap :")
    print(f"the first value is:{first_number}, the second value is:{second_number}")


##################################################################################################
# 3 . Write a python program to read two numbers and find the sum of their cubes
def task3():
    first_number = input_number("Please enter your first number :")
    second_number = input_number("Please enter your second number :")

    first_number_cubes = first_number * first_number * first_number
    second_number_cubes = second_number * second_number * second_number
    print("")
    print(f"Your first input cubes are  : {first_number}^3 = {first_number_cubes} ")
    print(f"Your second input cubes are  : {second_number}^3 = {second_number_cubes} ")
    print(f"The sum of both numbers is : {first_number_cubes + second_number_cubes}")


##################################################################################################
# 4 . Write a python program to read three numbers and if any two variables are equal , print that number
def task4():
    first_number = input_number("Please enter your first number :")
    second_number = input_number("Please enter your second number :")
    third_number = input_number("Please enter your third number :")
    print("")

    if first_number == second_number == third_number:
        print(f"All variables is equal to {first_number}")

    if first_number == second_number:
        print(f"The equal variables are the first input and the second input. \nthey equal to :{first_number}")

    elif first_number == third_number:
        print(f"The equal variables are the first input and the third input.\nthey equal to :{first_number}")

    elif second_number == third_number:
        print(f"The equal variables are the second input and the third input.\nthey equal to :{second_number}")
    else:
        print("No equal inputs ")


##################################################################################################
# 5 . Write a python program to read three numbers and find the smallest among them
def task5():
    first_number = input_number("Please enter your first number : ")
    second_number = input_number("Please enter your second number :")
    third_number = input_number("Please enter your third number :")

    if first_number < second_number and first_number < third_number:
        print(f"The smallest variable is the first input.\nthe number is : {first_number}")

    elif second_number < third_number:
        print(f"The smallest variable is the second input.\nthe number is :{second_number}")

    else:
        print(f"The smallest variable is the third input.\nthe number is : {third_number}")


##################################################################################################
# helper function

def input_number(text):
    number = input(text)
    while not number.isnumeric():
        number = input("Invalid input , " + text)

    return int(number)


def task_chooses(task):
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


##################################################################################################
# main

if __name__ == "__main__":
    another_task = "Y"
    while another_task == "Y" or another_task == "y":
        task = input_number("Please choose your task number (from 1 to 5) :")
        print("")
        task_chooses(task)
        print("")
        another_task = input("Do You Want to continue (Y/n) ")
        print("")

    print("The program go to the end ,Thank you :)")
