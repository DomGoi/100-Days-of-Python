from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Google:
    def __init__(self, adresy, ceny, linki):
        self.URL_FORMULARZ="https://docs.google.com/forms/d/e/1FAIpQLSdekN3TEQITq4dw9E0eiRbiyyRxxyzY0ktDAsR6ctqaw7eV_Q/viewform?usp=sf_link"
        self.lista_cen=ceny
        self.lista_adresów=adresy
        self.lista_lista=linki


        self.options=Options()
        self.options.add_experimental_option("detach", True)
        # self.options.add_argument("")
        # self.options.add_argument()

        self.driver = webdriver.Chrome(options=self.options)

    def insert_into_formularz(self):
        self.driver.get(self.URL_FORMULARZ)

        for a,p,l in zip(self.lista_adresów,self.lista_cen, self.lista_lista):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")))
            adres=self.driver.find_element(By.CSS_SELECTOR,"#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(1) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
            adres.send_keys(a)

            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")))
            cena=self.driver.find_element(By.CSS_SELECTOR,"#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(2) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
            cena.send_keys(p)

            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")))
            linki=self.driver.find_element(By.CSS_SELECTOR,"#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input")
            linki.send_keys(l)

            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div")))
            button=self.driver.find_element(By.CSS_SELECTOR,"#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div.DE3NNc.CekdCb > div.lRwqcd > div")
            button.click()

            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT,"Prześlij kolejną odpowiedź")))
            link_back=self.driver.find_element(By.PARTIAL_LINK_TEXT, "Prześlij kolejną odpowiedź").get_attribute("href")
            self.driver.get(link_back)




