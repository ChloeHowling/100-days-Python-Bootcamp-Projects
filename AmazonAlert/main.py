import smtplib
import ssl
import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/dp/B01MZBXVES/?coliid=I2JSJOQDUTT575&colid=1UV207K15NONS&psc=1&ref_=lv_ov_lig_dp_it_im"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Accept-Language": "en-us"
}

response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

price = float(soup.find(name="span", id="priceblock_ourprice").getText().split('$')[1])
item = "Rainbow Throw Blanket"
if price < 22:
    send_address = "elizabethwangwang@gmail.com"
    password = "Jilljill6"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
        server.login(send_address, password)
        server.sendmail(
            from_addr=send_address,
            to_addrs="chloehltam@gmail.com",
            msg=f"Subject: {item} Price Alert\n\nThe product price is now ${price}, below your target price. Buy now!\n"
                f"{url}"
        )

