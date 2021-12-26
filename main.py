from selenium import webdriver
import functions
import psycopg2
import os
import time 

DRIVER_PATH = '/home/vladimir/projects/webScrp/chromedriver'
LINKS = ('https://dennikn.sk/blog/','https://blog.sme.sk/','https://www.wikipedia.org/') # links for blogs
        

if __name__ == '__main__':

    user_opt = functions.get_user_input()

    # clearing the terminal

    os.system('cls||clear')

    # option 1, also choosing a link

    if user_opt == 1:

        user_opt = None

        print('There are three links to choose from : ')
        for index in (0,1,2):
            print(f'{index + 1} - {LINKS[index]}')

        while True:
            try:
                user_opt = int(input("what u wanna do ? "))
                if user_opt <= 0 or user_opt > 3:
                    continue
                break
            except ValueError:
                print('Give me an int...')

        
        print(LINKS[user_opt - 1])





#    driver = functions.open_driver(DRIVER_PATH)    


    # closing the driver
#    driver.close()