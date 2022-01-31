from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import databaseFunctions
import main
import time
import selenium
import os
import sys


# func for gettin users input (what choice)

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

# func for getting users input (how many)

def get_count(prompt):
    while True:
            try:
                count = int(input(prompt))
                if count < 0:
                    raise ValueError
                break
            except ValueError:
                print('Give me a valid value')
    
    return count


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

# waiting function for class name 
def wait_for_class_name(class_name, driver):
    try:
        myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
    except TimeoutException:
        print ("Loading took too much time!")
        sys.exit()

# allow cookies

def allow_cookies(driver, class_name = 'fc-button-label'):
    cookies = driver.find_element_by_class_name(class_name)
    cookies.click()
    print('Cookies clicked', end = '')

    for index in (0,1,2):
        print(".", end = '')
        sys.stdout.flush()
        time.sleep(0.5)

    os.system('cls||clear')

# function for getting demand what does user want to get

def get_demand():
    return input('What do you want to search for ? ')

# function for getting bool variable

def get_bool(prompt):
    while True:
        var = input(prompt).upper()
        if var == 'Y':
            return True
        elif var == 'N':
            return False
        else:
            print('wrong input')

# function for handling scraped data and writing them into a database

def handle_data(handled_data, product, product_name):
  
    # turning array prices into a float datatype
    n = len(handled_data)
    for i in range(n):
        for j in (0, 1):
            if handled_data[i][j] != 'Free':
                handled_data[i][j] = float(handled_data[i][j][: -1].replace(',', '.'))
            else:
                handled_data[i][j] = 0

    # bubble sorting array with prices ASC
    n = len(handled_data)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if handled_data[j][0] + handled_data[j][1] > handled_data[j + 1][0] + handled_data[j + 1][1]:
                handled_data[j], handled_data[j + 1] = handled_data[j + 1], handled_data[j]

    # saving data into a database

    conn = databaseFunctions.make_conn()

    databaseFunctions.insert_product(conn, handled_data, product, product_name)


