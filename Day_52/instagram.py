from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InstaFollower:
    def __init__(self, mail, password):
        self.URL_insta="https://www.instagram.com/"
        self.chrom_opt = webdriver.ChromeOptions()
        self.chrom_opt.add_experimental_option("detach", True)

        # Driver set-up
        self.driver = webdriver.Chrome(self.chrom_opt)
        self.login = mail
        self.password = password

    def perform_login(self):
        self.driver.get(self.URL_insta)

        # Rejecting cookies
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                         "body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x5yr21d.x19onx9a > div > button._a9--._ap36._a9_1")))
        reject_button = self.driver.find_element(By.CSS_SELECTOR, "body > div.x1n2onr6.xzkaem6 > "
                                                                  "div.x9f619.x1n2onr6.x1ja2u2z > div > "
                                                                  "div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x5yr21d.x19onx9a > div > button._a9--._ap36._a9_1")
        reject_button.click()

        # Inserting mail
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input")))
        login_mail = self.driver.find_element(By.CSS_SELECTOR,
                                              "#loginForm > div > div:nth-child(1) > div > label > input")
        login_mail.send_keys(self.login)

        # Inserting password
        password_mail = self.driver.find_element(By.CSS_SELECTOR,
                                                 "#loginForm > div > div:nth-child(2) > div > label > input")
        password_mail.send_keys(self.password)

        # clicking in log_in
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button")))
        button_login = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button")
        button_login.click()

        time.sleep(5)  # Wait for the page to load fully, you can adjust this value as needed
        turn_off_notifications = self.driver.find_element(By.CSS_SELECTOR, "body")
        turn_off_notifications.click()

    def find_followers(self,site_name):
        self.driver.get(f"{self.URL_insta}{site_name}/followers")

        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as an HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)





    def follow(self):
        # Check and update the (CSS) Selector for the "Follow" buttons as required.
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


