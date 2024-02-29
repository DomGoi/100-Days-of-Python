import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Start URL
URL="https://tinder.com/"

#Chrome options
chrom_opt=webdriver.ChromeOptions()
chrom_opt.add_experimental_option("detach", True)

driver=webdriver.Chrome(chrom_opt)
driver.get(URL)

#Rejecting cookies
time.sleep(2)
cookie_button=driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[2]/button")
cookie_button.click()

#Loggin in
time.sleep(5)
login_button=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a").get_attribute("href")
driver.get(login_button)

time.sleep(3)
google_log=driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[1]/div/div/div/iframe")
google_log.click()

#Switching to the new window
time.sleep(3)
all_windows=driver.window_handles
driver.switch_to.window(all_windows[-1])


#Logging into Google account
MAIL=os.environ("MAILMY")
PASSWORD=os.environ("MYPASSWORD")

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")))
mail_google=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
mail_google.send_keys(MAIL)
mail_google.send_keys(Keys.ENTER)

#Disabling the reCAPTCHAT manually
time.sleep(30)

#Inputing the password
pass_gog=driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
pass_gog.send_keys(PASSWORD)
pass_gog.send_keys(Keys.ENTER)

#Allowing the first pop-up
driver.switch_to.window(all_windows[0])
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[1]")))
allow_button=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[3]/button[1]")
allow_button.click()

#Rejecting second pop-up
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[1]")))
second_button=driver.find_element(By.XPATH,"/html/body/div[2]/main/div/div/div/div[3]/button[1]")
second_button.click()

#Starting like-loop for 100 likes
time.sleep(5)
for n in range(100):
    try:
        try:
            yes_tinder = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button")))
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button")))
            driver.execute_script("arguments[0].scrollIntoView();", yes_tinder)
            yes_tinder.click()

        #if the XPATH won't work, the key will be enabled
        except:
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_RIGHT)

    # When the match appears
    except ElementClickInterceptedException:
        try:

            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
            sleep(2)


        except NoSuchElementException:
            sleep(3)

#Closing browser after the liking process is finished
driver.quit()


