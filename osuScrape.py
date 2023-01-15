from bs4 import BeautifulSoup
from selenium import webdriver

import pandas

import math
import sys


# Gets the top plays given an id
def getTopPlays(id):
	driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

	driver.get(f'https://osu.ppy.sh/users/{id}')

	content = driver.page_source
	soup = BeautifulSoup(content)

	playLists = soup.findAll('div', attrs={'class':'play-detail-list u-relative'})

	topPlays = playLists[1];

	plays = [t.getText() for t in topPlays.findAll('a', attrs={'class': 'play-detail__title'})]
	accuracy = [t.getText() for t in topPlays.findAll('span', attrs={'class': 'play-detail__accuracy'})]
	mods = [t.get('data-acronym') for t in topPlays.findAll('div', attrs={'class': 'mod'})]
	pp = [t.getText() for t in topPlays.findAll('div', attrs={'class': 'play-detail__pp'})]

	print(plays)
	print(accuracy)
	print(mods)
	print(pp)

# Returns a player's rank given their id
def getPlayerRank(id):
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

    driver.get(f'https://osu.ppy.sh/users/{id}')

    content = driver.page_source
    soup = BeautifulSoup(content)

    return int(soup.find('div', attrs={'class':'value-display__value'}).text[1:])

# Returns top plays of players within 10% of a given rank
def getIds(id):
    lower = math.floor(getPlayerRank(id)*1.1)  # Players worse than
    higher = math.ceil(getPlayerRank(id)*0.9)  # Players better than

    print(lower)
    print(higher)

def main():
    getIds("SrChispa")

if __name__ == "__main__":
    main()

