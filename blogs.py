from calendar import WEDNESDAY
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import main
import selenium
import time
import os
import sys


def scrape_blog(driver, article_counter):

    # case user, chose dennikn blog
    if driver.current_url == main.LINKS[0]:
        cookies = driver.find_element_by_class_name('fc-button-label')
        cookies.click()
        print('Cookies clicked')


        os.chdir(os.path.join('/','home', 'vladimir' ,'projects', 'webScrp', 'articles', 'dennikn'))
#        file_names = driver.find_elements_by_tag_name('article')

        # creating text files... name of the file is authors name and date when he posted that
        for item in range(article_counter):

            # waiting for page to load
            try:
                myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'article')))
            except TimeoutException:
                print ("Loading took too much time!")
                sys.exit()

            file_names = driver.find_elements_by_tag_name('article')
            i = 0
            text_file_name = ''
            header_text = ''

            # while to determine filename
            while file_names[item].text[i: i + 4] != "2022":
                text_file_name += file_names[item].text[i]
                i += 1
            i += 5

            # while to determine header text
            while file_names[item].text[i] != '\n':
                header_text += file_names[item].text[i]
                if i == len(file_names[item].text) - 1:
                    break
                i += 1
    
            # waiting for page to load
            try:
                myElem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'p')))
            except TimeoutException:
                print ("Loading took too much time!")
                sys.exit()
            file_names[item].click()

            text = driver.find_elements_by_tag_name('p')

            # creating a file and writing the entire blog in it 

            with open(f'{text_file_name} 2022', 'w+') as article_file:
                article_file.write(f'{header_text} \n \n')
                for content in text:
                    writing_material = content.text.split()
                    row_len = 0
                    for word in writing_material:
                        article_file.write(f'{word} ')
                        row_len += 1

                        if row_len == 10:
                            article_file.write('\n')
                            row_len = 0
            driver.back()