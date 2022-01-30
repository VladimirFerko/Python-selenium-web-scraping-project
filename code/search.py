from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from google_images_download import google_images_download
import functions
import databaseFunctions
import os 


def search_it(driver, demand, wantDownl, count = -1):
    # creating history in postgres
    conn = databaseFunctions.make_conn()

    databaseFunctions.insert_search(conn, demand, wantDownl, count)


    # entering data
    search_bar = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    search_bar.send_keys(demand)
    search_bar.send_keys(Keys.ENTER)

    functions.wait_for_tag_name('h3', driver)


    # user wants to download pictures case

    if wantDownl:
        # changing directory
        os.chdir(os.path.join('/','home', 'vladimir' ,'projects', 'webScrp'))

        response = google_images_download.googleimagesdownload()
        args = {
            "keywords":     f'{demand}',
            "limit":        f'{count}',
            "print_urls":   False
        }

        paths = response.download(args)

        print(paths)

        

    
    
