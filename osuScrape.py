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

playLists = soup.findAll('div', attrs={'class':'play-detail-list u-relative'})

topPlays = playLists[1];

print(topPlays)

name = topPlays.findAll('a', attrs={'class': 'play-detail__title'})
acc = topPlays.findAll('span', attrs={'class': 'play-detail__accuracy'})

print(name)
print(acc)

"""
for div in soup.findAll('div', attrs={'class':'play-detail-list u-relative'}):
	name = div.find('div', attrs={'class': 'play-detail__title'})
	acc = div.find('div', attrs={'class': 'play-detail__accuracy'})
"""