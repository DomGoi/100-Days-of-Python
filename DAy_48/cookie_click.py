from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrom_opt=webdriver.ChromeOptions()
chrom_opt.add_experimental_option("detach", True)

driver=webdriver.Chrome(chrom_opt)
driver.get("http://orteil.dashnet.org/experiments/cookie/")


big_cookie=driver.find_element(By.CSS_SELECTOR, value="#cookie")


five_min=time.time()+5*60
timeout=time.time()+5

items_id=driver.find_elements(By.CSS_SELECTOR, "#store div ")
item_ids=[i.get_attribute("id") for i in items_id if i.text !=""]




while True:
    big_cookie.click()
    if time.time()>timeout:

        store = driver.find_elements(By.CSS_SELECTOR, "#store b")
        prices = [int(n.text.split("-")[1].strip().replace(",", "")) for n in store if "-" in n.text]

        store={}
        for n in range(len(prices)):
            store[prices[n]]=item_ids[n]
        #print(store)

        money_text = driver.find_element(By.CSS_SELECTOR, "#money").text
        if "," in money_text:
            money_text = money_text.replace(",", "")
        cookie_count = int(money_text)

        afford_upg={}
        for cost, id in store.items():
            if cookie_count>cost:
                afford_upg[cost]=id
        #print(afford_upg)

        highest_price=max(afford_upg)
        #print(highest_price)
        to_purchase=afford_upg[highest_price]

        driver.find_element(By.ID, to_purchase).click()

        timeout=time.time()+5

    if time.time() > five_min:
        cookie_per_sec = driver.find_element(By.ID, "cps").text
        print(cookie_per_sec)
        break
