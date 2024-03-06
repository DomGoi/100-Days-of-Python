import requests
from bs4 import BeautifulSoup


class Soup:
    def __init__(self):
        self.URL_ZILLO="https://appbrewery.github.io/Zillow-Clone/"


    def get_info(self):
        content=requests.get(self.URL_ZILLO)
        content.raise_for_status()
        site_html=content.text

        soup=BeautifulSoup(site_html,"html.parser")
        addresses_list=[]
        addresses=soup.find_all("address")
        for addr in addresses:
            addresses_list.append(addr.getText().strip())

        price_list=[]
        prices=soup.find_all(attrs={"data-test": "property-card-price"})
        for price in prices:
            price=price.getText().strip()
            price_list.append(price.split('/')[0].split('+')[0].split(' ')[0].replace(',', ''))

        links_list=[]
        links=soup.select(".StyledPropertyCardDataArea-anchor[data-test='property-card-link']")
        for link in links:
            links_list.append(link.get("href"))

        return addresses_list,price_list,links_list

