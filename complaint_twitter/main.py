from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bot import InternetSpeedTwitterBot


twitter_bot = InternetSpeedTwitterBot()
net_speed = twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()
