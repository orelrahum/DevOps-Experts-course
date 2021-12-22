# My Solution for bonus task 2
# Wrote By Orel Rahum

##################################################################################################
# 1 . Write a python program to swap two numbers using a third variable
def task1():
    for index in range(1, 11):
        print(index)


##################################################################################################
# 2 . Write a python program to swap two numbers without using third variable
# help : https://www.javatpoint.com/program-to-swap-two-numbers-without-using-the-third-variable
def task2():
    for index in range(1, 6):
        for index2 in range(1, index + 1):
            print(index2, end=" ")
        print("")


##################################################################################################
# 3 . Write a python program to read two numbers and find the sum of their cubes
def task3():
    sum = 0
    user_number = input_number("Please enter your your number :")

    for index in range(1, user_number + 1):
        sum += index
    print((f"Your Factorial number is : {sum}"))


##################################################################################################
# 4 . Write a python program to read three numbers and if any two variables are equal , print that number
def task4():
    list = []
    # number of elements as input
    n = int(input_number("Enter number of elements : "))

    # iterating till the range
    for i in range(1, n + 1):
        ele = int(input_number(f"Enter index {i} :"))

        list.append(ele)  # adding the element
    print(f"your Original List {list}\n")
    print(f"your Reversed List is:")
    for index in reversed(list):
        print(index)


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


##################################################################################################
# main

if __name__ == "__main__":
    another_task = "Y"
    while another_task == "Y" or another_task == "y":
        task = input_number("Please choose your task number (from 1 to 4) :")
        print("")
        task_chooses(task)
        print("")
        another_task = input("Do You Want to continue (Y/n) ")
        print("")

    print("The program go to the end ,Thank you :)")
