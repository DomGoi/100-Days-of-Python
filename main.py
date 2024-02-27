import time
import os
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Starting url- LinkeIn
URL="https://www.linkedin.com/jobs/search/?currentJobId=3816698390&f_AL=true&geoId=105072130&keywords=Biotechnologia&location=Polska&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"

#Saving the listing and following the company
def save_listing():
    for j in jobs:
        #Saving the listing
        driver.get(j)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div[2]/div/div/main/div/div[1]/div/div[1]/div/div/div[1]/div[4]/div/button')))
        save = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[2]/div/div/main/div/div[1]/div/div[1]/div/div/div[1]/div[4]/div/button')
        save.click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[3]/div[2]/div/div/main/div/div[1]/div/div[1]/div/div/div[1]/a')))
        #Following the companies site
        try:
            follow_site = driver.find_element(By.XPATH, '/html/body/div[6]/div[3]/div[2]/div/div/main/div/div[1]/div/div[1]/div/div/div[1]/a').get_attribute("href")
            driver.get(follow_site)
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/button[1]/svg/use")))
            try:
                follow_button=driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/button[1]/svg/use")
                follow_button.click()
            except:
                follow_button = driver.find_element(By.XPATH,"/html/body/div[6]/div[3]/div/div[2]/div/div[2]/main/div[1]/section/div/div[2]/div[2]/div[3]/div/div[1]/div[1]/button/svg/use")
                follow_button.click()


        except NoSuchElementException:
            print("Follow link not found.")


#Picking options for the webdriver
chrom_opt=webdriver.ChromeOptions()
chrom_opt.add_experimental_option("detach", True)


#Setting a driver and getting the started url
driver=webdriver.Chrome(options=chrom_opt)
driver.get(URL)
time.sleep(2)




#Rejecting cookies
cookie_button=driver.find_element(By.CSS_SELECTOR, "#artdeco-global-alert-container > div > section > div > div.artdeco-global-alert-action__wrapper > button:nth-child(2)")
cookie_button.click()
time.sleep(2)


#Logging into the account
MAIL=os.environ("MYMAIL")
HASLO=os.environ("MYHASLO")


buttin_sign=driver.find_element(By.LINK_TEXT, "Sign in")
buttin_sign.click()
wait = WebDriverWait(driver, 10)


#Typing the data for loggi'
username=wait.until(EC.visibility_of_element_located((By.ID, "username")))
username.send_keys(MAIL)


time.sleep(2)
password_type=wait.until(EC.visibility_of_element_located((By.ID, "password")))
password_type.send_keys(HASLO)
password_type.send_keys(Keys.ENTER)


#Closing down the chat
time.sleep(5)
try:
    button_down=driver.find_element(By.CSS_SELECTOR, '#ember39')
    button_down.click()
except:
    button_down = driver.find_element(By.CSS_SELECTOR, '#ember40')
    button_down.click()


#Getting links for all the jobs listed
job=driver.find_elements(By.CSS_SELECTOR," ul li div div div div div a")
jobs=[j.get_attribute("href") for j in job ]


save_listing()
driver.quit()

