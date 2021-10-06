from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import time

chrome_driver_path = "/Users/chloetam/Development/chromedriver"
url = "https://www.linkedin.com/jobs/search/?geoId=103644278&keywords=python%20developer&location=United%20States"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url=url)
login_btn = driver.find_element_by_class_name(name="nav__button-secondary")
login_btn.click()

time.sleep(0.5)

username = driver.find_element_by_css_selector("#username")
username.send_keys("chloehltam@gmail.com")
password = driver.find_element_by_css_selector("#password")
password.send_keys("Jilljill6")
password.send_keys(Keys.ENTER)

time.sleep(5)
while True:
    job_list = driver.find_elements_by_class_name(name="job-card-list")
    for item in job_list:
        ActionChains(driver).move_to_element(item).perform()
        try:
            item.click()
        # driver.execute_script(f"arguments[0].click();", item)
        except ElementClickInterceptedException:
            cross_btns = driver.find_elements_by_class_name(name="artdeco-toast-item__dismiss")
            for btn in cross_btns:
                btn.click()
                time.sleep(0.5)
            item.click()


        time.sleep(0.5)
        save_btn = driver.find_element_by_css_selector("button.jobs-save-button")
        save_btn.click()
        # driver.execute_script("arguments[0].click();", save_btn)
        time.sleep(0.5)
        print("Job saved")


