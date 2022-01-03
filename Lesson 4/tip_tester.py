from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

my_driver = webdriver.Chrome(executable_path='D:/selenium/chromedriver.exe')
my_driver.get(
    url='file:///D:/selenium/tip_calc/index.html')
#my_driver.find_elements(By.ID, "").
