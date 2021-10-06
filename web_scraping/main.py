from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import lxml
import time

CHROME_DRIVER_PATH = "/Users/chloetam/Development/chromedriver"
WEB_LINK = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSdeKo_YLu1EJSnstQP8dW5zsc5SbHmGkn5DItKK5QjoAtYzmw/viewform?usp=sf_link"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
    "Accept-Language": "en-us"
}
response = requests.get(url=WEB_LINK, headers=headers)
print(response)
soup = BeautifulSoup(response.text, 'lxml')
print(f"Retrieved: {soup.title.text}")

addresses = []
prices = []
links = []

infos = soup.find_all(class_="list-card-price")
for info in infos:
    prices.append(info.text.split('/')[0])

infos = soup.find_all(class_="list-card-link")
for info in infos:
    links.append(f"https://www.zillow.com{info['href']}")

infos = soup.find_all(class_="list-card-addr")
for info in infos:
    addresses.append(info.text)

print("Web info scraped.")

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

for n in range(len(links)):
    driver.get(FORM_LINK)
    time.sleep(1)

    address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')

    address.send_keys(addresses[n])
    price.send_keys(prices[n])
    link.send_keys(links[n])
    submit.click()


