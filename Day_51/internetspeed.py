import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InternetSpeedTwitterBot:
    def __init__(self, promised_down, promised_up):
        # Driver options
        self.chrom_opt = webdriver.ChromeOptions()
        self.chrom_opt.add_experimental_option("detach", True)

        # Driver set-up
        self.driver = webdriver.Chrome(self.chrom_opt)
        self.down=promised_down
        self.up=promised_up
        self.URL_SPEED="https://www.speedtest.net/"
        self.URL_Twitter="https://twitter.com/?lang=en"
        self.mail=os.environ("MAIL")
        self.password=os.environ("PASSWORD_TWITTER")
        self.name=os.environ("TWITTER_NAME")

    def get_internet_speed(self):
        self.driver.get(self.URL_SPEED)

        #Reject cookies
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[5]/div[2]/div/div/div[2]/div/div/button[1]")))
        reject=self.driver.find_element(By.XPATH, "/html/body/div[5]/div[2]/div/div/div[2]/div/div/button[1]")
        reject.click()

        #Running a test
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")))
        go_button=self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
        go_button.click()

        #Closing pop-up
        time.sleep(60) # time for the test to run
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button")))
        close_button=self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/p[2]/button")
        close_button.click()

        #Getting the download and upload speed as well as provider
        download_speed=self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        upload_speed=self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        provider=self.driver.find_element(By.XPATH,"/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[4]/div/div/div[1]/div[3]/div[2]").text
        return download_speed, upload_speed, provider



    def tweet_at_provider(self,download_speed,upload_speed,provider):
        self.driver.get(self.URL_Twitter)

        #Rejecting cookies
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div/div/div/div[1]/div/div/div/div/div/div[2]/div[2]")))
        reject_twitter_cookies=self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div/div/div/div/div/div[2]/div[2]")
        reject_twitter_cookies.click()


        #Logging in
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010 > main > div > div > div.css-175oi2r.r-tv6buo > div > div > div.css-175oi2r > div.css-175oi2r.r-2o02ov > a")))
        login=self.driver.find_element(By.CSS_SELECTOR,"#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010 > main > div > div > div.css-175oi2r.r-tv6buo > div > div > div.css-175oi2r > div.css-175oi2r.r-2o02ov > a")
        login.click()

        #Mail input
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#layers > div:nth-child(2) > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-kemksi.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-13qz1uu.r-1ye8kvj > div > div > div > div.css-175oi2r.r-1f1sjgu.r-mk0yit.r-13qz1uu > label > div > div.css-175oi2r.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input")))
        input_mail=self.driver.find_element(By.CSS_SELECTOR,"#layers > div:nth-child(2) > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-kemksi.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-13qz1uu.r-1ye8kvj > div > div > div > div.css-175oi2r.r-1f1sjgu.r-mk0yit.r-13qz1uu > label > div > div.css-175oi2r.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input")
        input_mail.send_keys(self.mail)
        input_mail.send_keys(Keys.ENTER)

        try:
            #password input
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#react-root > div > div > div > main > div > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox > div.css-175oi2r.r-16y2uox.r-1jgb5lz.r-13qz1uu.r-1ye8kvj > div.css-175oi2r.r-1fq43b1.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div > div.css-175oi2r.r-mk0yit.r-13qz1uu > div > label > div > div.css-175oi2r.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div.css-1rynq56.r-bcqeeo.r-qvutc0.r-37j5jr.r-135wba7.r-16dba41.r-1awozwy.r-6koalj.r-1inkyih.r-13qz1uu > input")))
            input_password=self.driver.find_element(By.CSS_SELECTOR,"#react-root > div > div > div > main > div > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox > div.css-175oi2r.r-16y2uox.r-1jgb5lz.r-13qz1uu.r-1ye8kvj > div.css-175oi2r.r-1fq43b1.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div > div.css-175oi2r.r-mk0yit.r-13qz1uu > div > label > div > div.css-175oi2r.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div.css-1rynq56.r-bcqeeo.r-qvutc0.r-37j5jr.r-135wba7.r-16dba41.r-1awozwy.r-6koalj.r-1inkyih.r-13qz1uu > input")
            input_password.send_keys(self.password)
            input_password.send_keys(Keys.ENTER)

        except:
            #name input
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#layers > div:nth-child(2) > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-kemksi.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-13qz1uu.r-1ye8kvj > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div.css-175oi2r.r-1f1sjgu.r-mk0yit > label > div > div.css-175oi2r.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input")))
            input_name=self.driver.find_element(By.CSS_SELECTOR,"#layers > div:nth-child(2) > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-kemksi.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-13qz1uu.r-1ye8kvj > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div.css-175oi2r.r-1f1sjgu.r-mk0yit > label > div > div.css-175oi2r.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input")
            input_name.send_keys(self.name)
            input_name.send_keys(Keys.ENTER)

            #password input
            WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#layers > div:nth-child(2) > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-kemksi.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-13qz1uu.r-1ye8kvj > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-175oi2r.r-mk0yit.r-13qz1uu > div > label > div > div.css-175oi2r.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div.css-1rynq56.r-bcqeeo.r-qvutc0.r-37j5jr.r-135wba7.r-16dba41.r-1awozwy.r-6koalj.r-1inkyih.r-13qz1uu > input")))
            input_password = self.driver.find_element(By.CSS_SELECTOR,"#layers > div:nth-child(2) > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-kemksi.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-13qz1uu.r-1ye8kvj > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-175oi2r.r-mk0yit.r-13qz1uu > div > label > div > div.css-175oi2r.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div.css-1rynq56.r-bcqeeo.r-qvutc0.r-37j5jr.r-135wba7.r-16dba41.r-1awozwy.r-6koalj.r-1inkyih.r-13qz1uu > input")
            input_password.send_keys(self.password)
            input_password.send_keys(Keys.ENTER)

            #Message
            WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div.css-175oi2r.r-kemksi.r-184en5c > div > div.css-175oi2r.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(1) > div > div > div > div > div > div > div > div > div > div > label > div.css-175oi2r.r-1wbh5a2.r-16y2uox > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div")))
            input_message=self.driver.find_element(By.CSS_SELECTOR,"#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div > div > div.css-175oi2r.r-kemksi.r-184en5c > div > div.css-175oi2r.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(1) > div > div > div > div > div > div > div > div > div > div > label > div.css-175oi2r.r-1wbh5a2.r-16y2uox > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div")
            input_message.click()
            time.sleep(3)
            input_message.send_keys(f"Hey {provider}, why is my internet speed {download_speed} Mbps/{upload_speed} Mbps when I pay for {self.down} Mbps/{self.up} Mbps?  #InternetSpeed #{provider}")

            WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']")))
            tweet_button = self.driver.find_element(By.XPATH, "//div[@data-testid='tweetButtonInline']")
            self.driver.execute_script("arguments[0].click();", tweet_button)

