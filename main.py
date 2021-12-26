from selenium import webdriver
import functions

DRIVER_PATH = '/home/vladimir/projects/webScrp/chromedriver'

if __name__ == '__main__':
    driver = functions.open_driver(DRIVER_PATH)




    # closing the driver
    driver.close()