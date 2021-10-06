from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "/Users/chloetam/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# url = "https://en.wikipedia.org/wiki/Main_Page"
url = "http://secure-retreat-92358.herokuapp.com"
driver.get(url=url)

# article_num = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# article_num.click()

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# search = driver.find_element_by_name("search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)

fname = driver.find_element_by_name("fName")
fname.send_keys("Chloe")
lname = driver.find_element_by_name("lName")
lname.send_keys("Tam")
email = driver.find_element_by_name("email")
email.send_keys("chloehltam@gmail.com")
email.send_keys(Keys.ENTER)
# driver.quit()