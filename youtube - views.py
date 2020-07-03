from selenium import webdriver
from random import randrange
import time

refresh_time = 10
browser_list = []

browser_1 = webdriver.Chrome("C:\Users\AL2331\Downloads\chromedriver\chromedriver")
browser_2 = webdriver.Chrome("C:\Users\AL2331\Downloads\chromedriver\chromedriver")
browser_3 = webdriver.Chrome("C:\Users\AL2331\Downloads\chromedriver\chromedriver")
browser_4 = webdriver.Chrome("C:\Users\AL2331\Downloads\chromedriver\chromedriver")
browser_5 = webdriver.Chrome("C:\Users\AL2331\Downloads\chromedriver\chromedriver")

browser_list.append(browser_1)
browser_list.append(browser_2)
browser_list.append(browser_3)
browser_list.append(browser_4)
browser_list.append(browser_5)

for browser in browser_list:
	browser.get("https://www.youtube.com/watch?v=fZo6futIKmI&t=20s")

while(True):
	browser_num = randrange(0, len(browser_list))	
	browser_list[browser_num].refresh()
	time.sleep(refresh_time)