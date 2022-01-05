# My Solution for bonus task 4
# Wrote By Orel Rahum
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


##################################################################################################
# 1 .
def task1():
    driver = webdriver.Chrome(executable_path="selenium_Drivers/chromedriver.exe")
    driver.get("http://www.walla.co.il")
    driver_firefox = webdriver.Firefox(executable_path="selenium_Drivers/geckodriver.exe")
    driver_firefox.get("http://www.ynet.co.il")


##################################################################################################
# 2 .
def task2():
    driver = webdriver.Chrome(executable_path="selenium_Drivers/chromedriver.exe")
    driver.get("http://www.walla.co.il")
    website_title = driver.title
    print(website_title)
    driver.refresh()
    if driver.title == website_title:
        print("pass")
    else:
        print("no")


##################################################################################################
# 3 .yes - elements are the same regardless to the browser
def task3():
    print("yes - elements will be the same ")


##################################################################################################
# 4 .
def task4():
    driver = webdriver.Chrome(executable_path="selenium_Drivers/chromedriver.exe")
    driver.get("https://translate.google.com/")
    driver.find_element(By.ID, "").send_keys("בדיקה")
    driver.find_element(By.ID, "").click()


##################################################################################################
# 5 .
def task5():
    driver = webdriver.Chrome(executable_path="selenium_Drivers/chromedriver.exe")
    driver.get("https://www.youtube.com/")
    driver.find_element(By.ID,"search").send_keys("check")
    driver.find_element(By.ID, "search-icon-legacy").click()


##################################################################################################
# 6 .
def task6():
    driver = webdriver.Chrome(executable_path="selenium_Drivers/chromedriver.exe")
    driver.get("https://translate.google.com/")


##################################################################################################
# 7 .
def task7():
    driver = webdriver.Chrome(executable_path="selenium_Drivers/chromedriver.exe")
    driver.get("https://www.facebook.com/")
    driver.find_element(By.ID, "email").send_keys("a@a.com")
    driver.find_element(By.ID, "pass").send_keys("Aa123456")


##################################################################################################
# 8 .
def task8():
    print("No finish yet")
    pass


##################################################################################################
# 9 .
def task9():
    print("No finish yet")
    pass


##################################################################################################
# 10 .
def task10():
    print("No finish yet")
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
