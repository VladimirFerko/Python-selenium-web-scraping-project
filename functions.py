from selenium import webdriver
import time


# function for opening google chrome driver 

def open_driver(DRIVER_PATH):
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get("https://www.facebook.com/")
    time.sleep(4)
    return driver