from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys
import time
timeout = time.time() + (60*5)

chrome_driver_path = "/Users/chloetam/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# url = "https://orteil.dashnet.org/cookieclicker/"
#
# driver.get(url=url)
# big_cookie = driver.find_element_by_id("bigCookie")
# products = driver.find_elements_by_css_selector(".enabled.price")
#
# shop_timer = time.time() + 5
# while True:
#     if time.time() > shop_timer:
#         products = driver.find_elements_by_css_selector(".enabled span.price")
#         product_num = products[-1].get_attribute("id")[-1]
#         product = driver.find_element_by_id(f"product{product_num}")
#         print(product.text)
#
#
#         shop_timer = time.time() + 5
#     if time.time() > timeout:
#         break
#     big_cookie.click()

ignored_exception = StaleElementReferenceException

url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url=url)
big_cookie = driver.find_element_by_id("cookie")

shop_timer = time.time() + 5
while True:
    if time.time() > shop_timer:
        money = driver.find_element_by_id("money").text
        for item in driver.find_elements_by_css_selector("#store div")[::-1]:
            if item.get_attribute("class") != "grayed":
                print(f"Bought: {item.text}")
                item.click()
                break
        shop_timer = time.time() + 5
    if time.time() > timeout:
        print(f"Money left: {driver.find_element_by_id('money').text}")
        print(driver.find_element_by_id("cps").text)
        break
    big_cookie.click()

