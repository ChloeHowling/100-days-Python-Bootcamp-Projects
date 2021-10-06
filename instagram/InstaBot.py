from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time


CHROME_DRIVER_PATH = "/Users/chloetam/Development/chromedriver"
EMAIL = "zeilbtam@gmail.com"
PASSWORD = "Jilljill6@"
SIMILAR_ACCOUNT = "pixelgustavo"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get(url="https://www.instagram.com")
        time.sleep(0.5)
        input_box = self.driver.find_element_by_name("username")
        input_box.send_keys(EMAIL)
        input_box = self.driver.find_element_by_name("password")
        input_box.send_keys(PASSWORD)
        input_box.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        # btn = self.driver.find_element_by_link_text("Not Now")
        # if btn:
        #     btn.click()

        search_bar = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.send_keys(SIMILAR_ACCOUNT)
        time.sleep(1)
        search_bar.send_keys(Keys.ENTER)
        search_bar.send_keys(Keys.ENTER)
        time.sleep(1)
        self.driver.find_element_by_partial_link_text("followers").click()
        time.sleep(3)

    def follow(self):
        while True:
            btn = self.driver.find_element_by_xpath('//button[text()="Follow"]')
            try:
                btn.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_btn = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_btn.click()