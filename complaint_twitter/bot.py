from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

SPEED_DOWN = 150
SPEED_UP = 10
CHROME_DRIVER_PATH = "/Users/chloetam/Development/chromedriver"
TWITTER_EMAIL = "zeilbtam@gmail.com"
TWITTER_PASSWORD = "Jilljill6@@@"
SPEED_SITE = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.down = SPEED_DOWN
        self.up = SPEED_UP

    def get_internet_speed(self):
        self.driver.get(SPEED_SITE)
        button = self.driver.find_element_by_class_name("start-text")
        button.click()
        time.sleep(45)
        self.down = self.driver.find_element_by_css_selector(".download-speed").text
        self.up = self.driver.find_element_by_css_selector(".upload-speed").text
        print(f"Download speed: {self.down} Mbps")
        print(f"Upload speed: {self.up} Mbps")


    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]').click()
        input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        input.send_keys(TWITTER_EMAIL)
        input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label')
        input.send_keys(TWITTER_PASSWORD)
        input.send_keys(Keys.ENTER)
        time.sleep(1)

        message = f"Hey Internet Provider, why is my internet speed " \
                  f"{self.down}down/{self.up}up when I pay for 150down/10up?"

        box = self.driver.find_element_by_class_name("public-DraftStyleDefault-block")
        box.send_keys(message)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span').click()


