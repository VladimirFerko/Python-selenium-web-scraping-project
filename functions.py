from selenium import webdriver
import time


# func for gettin users input

def get_user_input():
    
    print('hi, there are your options to choose from')
    print('1 - scrape text from a blog\n2 - search something in google\n3 - compare prices on heureka')

    while True:
        try:
            option = int(input("what u wanna do ? "))
            if option <= 0 or option > 3:
                continue
            break
        except ValueError:
            print('Give me an int...')

    return option



# function for opening google chrome driver 

def open_driver(DRIVER_PATH):
    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get("https://www.google.com/")
    time.sleep(4)
    return driver