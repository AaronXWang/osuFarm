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
for a in soup.findAll(attrs={'class':'play-detail play-detail--highlightable'}):
    name = a.find('div', attrs={'class':'play-detail__title u-ellipsis-overflow'})
    plays.append(name.text)
