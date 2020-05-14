import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")

driverCrm = webdriver.Chrome(executable_path='chromedriver/chromedriver.exe', chrome_options=chrome_options)

# Get into linked result of google search and try to login
driverCrm.get("http://localhost:8081")