# My Solution for bonus task 4
# Wrote By Orel Rahum
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


##################################################################################################

driver = webdriver.Chrome(executable_path="selenium_Drivers/chromedriver.exe")
driver.get("http://www.walla.co.il")
driver_firefox = webdriver.Firefox(executable_path="selenium_Drivers/geckodriver.exe")
driver_firefox.get("http://www.ynet.co.il")

