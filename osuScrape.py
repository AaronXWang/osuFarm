from bs4 import BeautifulSoup
import pandas
from selenium import webdriver

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
listings = []
prices = []

driver.get("https://www.pathofexile.com/trade/exchange/Sanctum/Nn8Vt0")