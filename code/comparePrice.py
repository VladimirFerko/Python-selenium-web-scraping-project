from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import functions

def insert_product(driver, product):

    # entering demand
    search_box = driver.find_element(By.XPATH, '//*[@id="rootHead"]/form/input')
    search_box.send_keys(product)
    search_box.send_keys(Keys.ENTER)

    functions.wait_for_class_name('c-product-list__item', driver)

    clickable_product = driver.find_element(By.CLASS_NAME, 'c-product-list__item')
    clickable_product.click()

def get_prices(driver):
    prices = driver.find_element_by_class_name('c-offers-list')
    product_name = driver.find_element(By.XPATH, '//*[@id="__next"]/main/div/div[1]/div/div[1]/div[2]/h1')
    scraped_arr = prices.text.split()


    tmp = list()
    handled_data = list()
    print(scraped_arr)
    for index in range(len(scraped_arr)):
        if scraped_arr[index] == "€":
            price = f'{scraped_arr[index - 1]} {scraped_arr[index]}'
            tmp.append(price)
            continue
        if scraped_arr[index] == 'zdarma':
            tmp.append('Free')
            continue
        if scraped_arr[index] == 'obchodu':
            if not '.' in scraped_arr[index + 1] and index + 2 < len(scraped_arr):
                tmp.append(f'{scraped_arr[index + 1]} {scraped_arr[index + 2]}')
            else:
                tmp.append(scraped_arr[index + 1])
            handled_data.append(tmp)
            tmp = list()
    
    return handled_data, product_name
