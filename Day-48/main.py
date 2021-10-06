from selenium import webdriver

chrome_driver_path = "/Users/chloetam/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# url = "https://www.amazon.com/dp/B01MZBXVES/?coliid=I2JSJOQDUTT575&colid=1UV207K15NONS&psc=1&ref_=lv_ov_lig_dp_it_im"
url = "https://python.org/"
driver.get(url)
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)

# doc_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(doc_link.text)

# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)


event_times = driver.find_elements_by_css_selector(".medium-widget.event-widget.last div ul li")
events_dict = {}
for n, items in enumerate(event_times):
    info = items.text.split('\n')
    events_dict[n] = {"time": info[0], "name": info[1]}

print(events_dict)

# driver.close()
driver.quit()

