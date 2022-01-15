from selenium import webdriver
import functions
import blogs
import psycopg2
import os
import time 
import sys

DRIVER_PATH = '/home/vladimir/projects/webScrp/chromedriver'
LINKS = ('https://dennikn.sk/blog/','https://blog.sme.sk/','https://www.wikipedia.org/') # links for blogs
        

if __name__ == '__main__':

    user_opt = functions.get_user_input()

    # clearing the terminal
    print('\nLoading', end = '')

    for index in (0,1,2):
        print(".", end = '')
        sys.stdout.flush()
        time.sleep(1)
    os.system('cls||clear')

    # option 1, also choosing a link

    if user_opt == 1:

        user_opt = None

        print('There are three links to choose from : ')
        for index, item in enumerate(LINKS):
            print(f'{index + 1} - {item}')

        while True:
            try:
                user_opt = int(input("which website do you want to choose ? "))
                if user_opt <= 0 or user_opt > 3:
                    continue
                break
            except ValueError:
                print('Give me an int...')

        driver = functions.open_driver(DRIVER_PATH, LINKS[user_opt - 1])    

        blogs.scrape_blog(driver)


    # closing the driver
    driver.close()