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

name = topPlays.findAll('a', attrs={'class': 'play-detail__title'})
acc = topPlays.findAll('span', attrs={'class': 'play-detail__accuracy'})
mods = topPlays.findAll('div', attrs={'class': 'mod'})
pp = topPlays.findAll('div', attrs={'class': 'play-detail__pp'})

print(name)
print(acc)
print(mods)
print(pp)

"""
for div in soup.findAll('div', attrs={'class':'play-detail-list u-relative'}):
	name = div.find('div', attrs={'class': 'play-detail__title'})
	acc = div.find('div', attrs={'class': 'play-detail__accuracy'})
"""