from calendar import WEDNESDAY
from pydoc_data.topics import topics
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import main
import functions
import selenium
import time
import os
import sys


def scrape_blog(driver, article_counter):

    # array for article elements
    article_arr = [None] * article_counter

    # case user, chose dennikn blog
    if driver.current_url == main.LINKS[0]:
        print('The blog you have chosen : dennikn.sk')

        # allow cookies
        functions.allow_cookies(driver)

        # changing directory for files
        os.chdir(os.path.join('/','home', 'vladimir' ,'projects', 'webScrp', 'articles', 'dennikn'))

        # creating text files... name of the file is authors name and date when he posted that
        for item in range(article_counter):

            # waiting func for articles to load
            functions.wait_for_tag_name('article', driver)

            for i in range(article_counter):
                article_arr[i] = driver.find_element_by_tag_name('article')

            print(article_arr)
            i = 0
            text_file_name = ''
            header_text = ''

            # while to determine filename
            while article_arr[item].text[i: i + 4] != "2022":
                text_file_name += article_arr[item].text[i]
                i += 1
            i += 5

            # while to determine header text
            while article_arr[item].text[i] != '\n':
                header_text += article_arr[item].text[i]
                if i == len(article_arr[item].text) - 1:
                    break
                i += 1
    
            # waiting for page to load
            functions.wait_for_tag_name('p', driver)
            
            article_arr[item].click()

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



    # case user has chosen blog sme
    elif driver.current_url == main.LINKS[1]:
        print('The blog you have chosen : blog.sme.sk')
        # allow cookies
        functions.allow_cookies(driver)

        # changing directory for files
        os.chdir(os.path.join('/','home', 'vladimir' ,'projects', 'webScrp', 'articles', 'sme'))

        # determining what topic does the user want
        toppics = driver.find_elements_by_class_name('nav-item')

        # printing the options and getting the toppic
        print('Select the topic of your choice : ')
        for index,item in enumerate(toppics):
            print(f'{index + 1} - {item.text}')

        toppic_choice = functions.get_user_input('Choose a topic of a blog you want to scrape : ', 11)

        print(f'you have chosen {toppics[toppic_choice - 1].text}')

        for item in range(article_counter):
            toppics = driver.find_elements_by_class_name('nav-item')
            # waiting for page to load and clicking on certain element
            functions.wait_for_class_name('nav-link', driver)
            toppics[toppic_choice - 1].click()

            functions.wait_for_tag_name('h3', driver)

            for i in range(article_counter):
                article_arr[i] = driver.find_element_by_tag_name('h3')

            # clicking on an elements of the articles and scraping them
            article_arr[item].click()

            # items to write in the file
            header_text = driver.find_element_by_tag_name('h1')
            text = driver.find_elements_by_tag_name('p')
            file_name = driver.find_element_by_class_name('name')
            

            # writing down the stuff
            with open(file_name.text, 'w+') as article:
                article.write(header_text.text)
                article.write('\n\n')

                for content in text:
                    writable_text = content.text.split()
                    print(writable_text)
                    row_len = 0
                    for word in writable_text:
                        article.write(f'{word} ')
                        row_len += 1

                        if row_len == 10:
                            article.write('\n')
                            row_len = 0
            
            driver.back()




            
