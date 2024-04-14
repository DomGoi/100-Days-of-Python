import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class PyScale:
    def __init__(self):
        self.URL_PAYSCALE="https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
        self.chrom_options=webdriver.ChromeOptions()
        self.chrom_options.add_experimental_option("detach", True)

        #Driver set-up
        self.driver=webdriver.Chrome(self.chrom_options)
        self.payscale_data=[]

    def go_to_site(self):
        self.driver.get(self.URL_PAYSCALE)

    def get_data(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(
            (By.XPATH, "//tr[@class='data-table__row']")
        ))

        rows = self.driver.find_elements(By.XPATH, "//tr[@class='data-table__row']")
        page_data={}
        for row in rows:

            try:
                rank = row.find_element(By.XPATH,
                                        ".//td[contains(@class, 'csr-col--rank')]//span[@class='data-table__value']").text
            except NoSuchElementException:
                rank = "Not available"

            try:
                major = row.find_element(By.XPATH,
                                         ".//td[contains(@class, 'csr-col--school-name')]//span[@class='data-table__value']").text
            except NoSuchElementException:
                major = "Not available"

            try:
                early_career_pay = row.find_element(By.XPATH,
                                                    ".//td[contains(@class, 'csr-col--right')][1]//span[@class='data-table__value']").text
            except NoSuchElementException:
                early_career_pay = "Not available"

            try:
                mid_career_pay = row.find_element(By.XPATH,
                                                  ".//td[contains(@class, 'csr-col--right')][2]//span[@class='data-table__value']").text
            except NoSuchElementException:
                mid_career_pay = "Not available"

            try:
                high_meaning = row.find_element(By.XPATH,
                                                ".//td[contains(@class, 'csr-col--right')][3]//span[@class='data-table__value']").text
            except NoSuchElementException:
                high_meaning = "Not available"

            page_data[rank]= {
                "Major": major,
                "Early Career Pay": early_career_pay,
                "Mid-Career Pay": mid_career_pay,
                "% High Meaning": high_meaning
            }
        self.payscale_data.append(page_data)

        return page_data, self.payscale_data
    def is_the_next_button_active(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#__next > div > div.content--full-width > article > div.pagination.csr-gridpage__pagination > a.pagination__btn.pagination__next-btn')
            ))

            # Find the element
            next_button = self.driver.find_element(By.CSS_SELECTOR, '#__next > div > div.content--full-width > article > div.pagination.csr-gridpage__pagination > a.pagination__btn.pagination__next-btn')
            href = next_button.get_attribute("href")

            return href

        except Exception as e:
            print("Error checking next button state:", e)
            return False


    def next_page(self):

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#__next > div > div.content--full-width > article > div.pagination.csr-gridpage__pagination > a.pagination__btn.pagination__next-btn")
        ))

        next_button=self.driver.find_element(By.CSS_SELECTOR,"#__next > div > div.content--full-width > article > div.pagination.csr-gridpage__pagination > a.pagination__btn.pagination__next-btn")
        next_button.click()

    def save_data_to_csv(self, csv_file):
        fieldnames = ['Major', 'Early Career Pay', 'Mid-Career Pay', '% High Meaning']

        with open(csv_file, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            # Flatten the data to write to CSV
            for majors in self.payscale_data:
                for major_data in majors.values():
                    writer.writerow(major_data)

        return csv_file


    def close_driver(self):
        self.driver.quit()

