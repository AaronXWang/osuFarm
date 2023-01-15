from bs4 import BeautifulSoup
import pandas
from selenium import webdriver

driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

plays = []
accuracy = []
mods = []
pp = []

driver.get("https://osu.ppy.sh/users/11403312")

content = driver.page_source
soup = BeautifulSoup(content)
for i in soup.findAll('a', href=True, attrs={'class':'play-detail-list u-relative'}):
    name=a.find('div', attrs={'class':})