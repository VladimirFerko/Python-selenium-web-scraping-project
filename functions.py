from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import main
import main
import selenium
import time
import selenium
import os
import sys


# func for gettin users input

def get_user_input(prompt, high_limit,low_limit = 0):
    
    while True:
        try:
            option = int(input(prompt))
            if option <= low_limit or option > high_limit:
                continue
            break
        except ValueError:
            print('Give me an int...')

    os.system('cls||clear')

    return option


# function for opening google chrome driver 

def open_driver(DRIVER_PATH, link = 'https://www.google.com/'):
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(link)
    return driver

# waiting function for tag name

def wait_for_tag_name(tag_name, driver):
    # waiting for page to load
            try:
                myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, tag_name)))
            except TimeoutException:
                print ("Loading took too much time!")
                sys.exit()

# allow cookies

def allow_cookies(driver):
    cookies = driver.find_element_by_class_name('fc-button-label')
    cookies.click()
    print('Cookies clicked', end = '')

    for index in (0,1,2):
        print(".", end = '')
        sys.stdout.flush()
        time.sleep(0.5)

    os.system('cls||clear')