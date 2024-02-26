from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrom_opt=webdriver.ChromeOptions()
chrom_opt.add_experimental_option("detach", True)


driver=webdriver.Chrome(options=chrom_opt)
driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name=driver.find_element(By.NAME, "fName")
f_name.send_keys("Maria")
l_name=driver.find_element(By.NAME, "lName")
l_name.send_keys("Bogota")
email=driver.find_element(By.NAME, "email")
email.send_keys("mbogota@wp.pl")
email.send_keys(Keys.ENTER)
