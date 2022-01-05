# My Solution for bonus task 4
# Wrote By Orel Rahum

##################################################################################################
# 1 .
def task1():
    pass


##################################################################################################
# 2 .
def task2():
    pass


##################################################################################################
# 3 .
def task3():
    pass


##################################################################################################
# 4 .
def task4():
    pass


##################################################################################################
# 5 .
def task5():
    pass


##################################################################################################
# 6 .
def task6():
    pass


##################################################################################################
# 7 .
def task7():
    pass


##################################################################################################
# 8 .
def task8():
    pass


##################################################################################################
# 9 .
def task9():
    pass


##################################################################################################
# 10 .
def task10():
    pass


##################################################################################################
# helper function

def input_number_with_range(text, start, end):
    while True:
        try:
            number = int(input(text))
            assert start <= number <= end
        except ValueError:
            print("Not an integer! Please enter an integer.\n")
        except AssertionError:
            print(f"Please enter an integer between {start} and {end}\n")
        else:
            break

    return number


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
    elif task == 6:
        task6()
    elif task == 7:
        task7()
    elif task == 8:
        task8()
    elif task == 9:
        task9()
    elif task == 10:
        task10()


##################################################################################################
# main

if __name__ == "__main__":
    another_task = "Y"
    while another_task == "Y" or another_task == "y":
        task = input_number_with_range("Please choose your task number (from 1 to 10) :", 1, 10)
        print("")
        task_chooses(task)
        print("")
        another_task = input("Do You Want to continue (Y/n) ")
        print("")

    print("The program go to the end ,Thank you :)")
