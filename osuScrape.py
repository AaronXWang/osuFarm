from bs4 import BeautifulSoup
import pandas
from selenium import webdriver

import sys

def getTopPlays(id):
	driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

	plays = []
	accuracy = []
	mods = []
	pp = []

	driver.get(f'https://osu.ppy.sh/users/{id}')

	content = driver.page_source
	soup = BeautifulSoup(content)

	playLists = soup.findAll('div', attrs={'class':'play-detail-list u-relative'})

	topPlays = playLists[1];

	name = [t.getText() for t in topPlays.findAll('a', attrs={'class': 'play-detail__title'})]
	acc = [t.getText() for t in topPlays.findAll('span', attrs={'class': 'play-detail__accuracy'})]
	mods = [t.get('data-acronym') for t in topPlays.findAll('div', attrs={'class': 'mod'})]
	pp = [t.getText() for t in topPlays.findAll('div', attrs={'class': 'play-detail__pp'})]

	print(name)
	print(acc)
	print(mods)
	print(pp)


def main(player_id):
	getTopPlays(player_id)

if __name__ == "__main__":
	args = sys.argv

	if len(args) != 2:
		print(f'Wrong number of arguments: Expected 1, received {len(args)-1}')
	else:
		main(args[1])

