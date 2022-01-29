from tokenize import Name
from selenium import webdriver
from selenium.webdriver.common.by import By
import functions
import blogs
import search
import psycopg2
import os
import time 
import sys

DRIVER_PATH = '/home/vladimir/projects/webScrp/chromedriver'
LINKS = ('https://dennikn.sk/blog/','https://blog.sme.sk/','https://www.wikipedia.org/') # links for blogs
        

if __name__ == '__main__':

    # getting input from the user

    print('hi, there are your options to choose from')
    print('1 - scrape text from a blog\n2 - search something in google\n3 - compare prices on heureka')
    user_opt = functions.get_user_input("what u wanna do ? ", 3)

    # loading print with some delay
    print('Loading', end = '')

    for index in (0,1,2):
        print(".", end = '')
        sys.stdout.flush()
        time.sleep(0.5)

    os.system('cls||clear')
    

    # option 1, also choosing a link

    if user_opt == 1:

        user_opt = None

        print('There are three links to choose from : ')
        for index, item in enumerate(LINKS):
            print(f'{index + 1} - {item}')

        # determining which webside does user want to use

        user_opt = functions.get_user_input("which website do you want to choose ? ", 3)
        

        # determining how many articles does user want to scrape or what demand does user want to scrape

        if user_opt != 3:
            article_counter = functions.get_count('How many articles do you want to scrape ? ')
        else:
            demand = functions.get_demand()
        driver = functions.open_driver(DRIVER_PATH, LINKS[user_opt - 1])    


        if driver.current_url != LINKS[2]:
            blogs.scrape_blog(driver, article_counter)
        else:
            blogs.scrape_blog(driver, demand)
    
    elif user_opt == 2:

        # getting user input
        demand = functions.get_demand()

        # asking if the user want to download some photos 
        wantDownl = functions.get_bool('Do you want to download the images of the demand ? [Y/n] ')

        if wantDownl:
            count = functions.get_count('How many ? ')

        # clicking cookies
        driver = functions.open_driver(DRIVER_PATH)
        driver.find_element(By.XPATH,'//*[@id="L2AGLb"]').click()

        

        # scraping function
        try:
            search.search_it(driver, demand, wantDownl, count)
        except NameError:
            search.search_it(driver, demand, wantDownl)

        

    # closing the driver
    driver.close()