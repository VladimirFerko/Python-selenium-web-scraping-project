from selenium import webdriver
import main
import selenium
import time
import os


def scrape_blog(driver):

    # case user, chose dennikn blog
    if driver.current_url == main.LINKS[0]:
        cookies = driver.find_element_by_class_name('fc-button-label')
        cookies.click()
        print('Cookies clicked')

        # determining how many articles does user want to scrape

        while True:
            try:
                article_counter = int(input('How many articles do you want to scrape ? '))
                if article_counter < 0:
                    raise ValueError
                break
            except ValueError:
                print('Give me a valid value')

        file_names = driver.find_elements_by_tag_name('article')
        os.chdir(os.path.join('/','home', 'vladimir' ,'projects', 'webScrp', 'articles', 'dennikn'))


        # creating text files... name of the file is authors name and date when he posted that

        for item in range(article_counter):
            i = 0
            text_file_name = ''
            while file_names[item].text[i: i + 4] != "2022":
                text_file_name += file_names[item].text[i]
                i += 1
            file_names[item].click()
            driver.implicitly_wait(5)
            text = driver.find_elements_by_tag_name('p')

            # creating a file and writing the entire blog in it 

            with open(f'{text_file_name} 2022', 'w+') as article_file:
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
            time.sleep(2)