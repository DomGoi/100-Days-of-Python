import requests
from bs4 import BeautifulSoup
import smtplib
import os

URL_AMAZON="https://www.amazon.com/Garmin-v%C3%ADvoactive-Smartwatch-Contactless-Payments/dp/B07CVJ68GP/ref=sr_1_7?_encoding=UTF8&content-id=amzn1.sym.33f8f65b-b95c-44af-8b89-e59e69e79828&dib=eyJ2IjoiMSJ9.k4gtnQ8J8dmzr1QnsTHzVE5cZ1B5rzdSVcJ_agHzOACVOXmcuDBE0Zat5VsRrjATIA9yfibaNDKqlAS5poW2vmNT4x3Ha9C7j5Nn5DoH9Xr2AP11bt51ZrvRxhWBd39cLNyUPR5deVu563ujVYm2SXvqanZLCvaLe21RpZ6PFOaHteFJcFky7g-W1Ox5cCU5CLDkkrTOc4L1iBuUagWTB6M6JrpjmhsTUbcNPUYYkE_dXV-b25zjH3IX6BvfRuCCrqlz1YKBye7W22Yg8PJpVFum3XdbqSb_-U2e8voI9uY.7WC6kQCVMBv1lazekV_Vq0ek5jVkhTJ4vL2Vp1WyNcU&dib_tag=se&keywords=activity+trackers+and+smartwatches&pd_rd_r=e8d9bbde-4f55-4652-9f4a-f8c5ab0145fe&pd_rd_w=esiwS&pd_rd_wg=Du5wX&pf_rd_p=33f8f65b-b95c-44af-8b89-e59e69e79828&pf_rd_r=W2W3MZQ446765XBF9BN1&qid=1708792429&refinements=p_123%3A222211%2Cp_72%3A1248879011&rnid=1248877011&s=wearable-tech&sr=1-7"
TARGET_PRICE=129.99
paramsi={
"User-Agent":os.environ("USER_AGENT"),
"Accept-Language":os.environ("language")
}
#Getting the HTML "soup"
resource=requests.get(URL_AMAZON, headers=paramsi)
resource.raise_for_status()
amazon_code=resource.text

soup=BeautifulSoup(amazon_code,"lxml")

#Getting the price
price_whole = soup.find('span', {'class': 'a-price-whole'})
price_decimal = soup.find('span', {'class': 'a-price-fraction'})# Using a more specific class
name_product=soup.find(name="span", id="productTitle")
product_name=name_product.getText().strip()


if price_whole:
    price_amazon = float(f"{price_whole.getText().strip()}{price_decimal.getText().strip()}")
    if price_amazon<TARGET_PRICE:
        mymail = os.environ("mymail")
        password = os.environ("password_mail")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=mymail, password=password)
            connection.sendmail(from_addr=mymail, to_addrs=mymail,
                                msg=(f"Subject: Price of Garmin watch dropped \n\n Hey the price of the {product_name} dropped to ${price_amazon}. Buy Now!").encode('utf-8'))
else:
    print("Price not found.")