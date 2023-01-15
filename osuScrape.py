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
    soup = BeautifulSoup(content, features="html.parser")

    playLists = soup.findAll('div', attrs={'class':'play-detail-list u-relative'})

    topPlays = playLists[1];

    plays = [t.getText() for t in topPlays.findAll('a', attrs={'class': 'play-detail__title'})]
    accuracy = [t.getText() for t in topPlays.findAll('span', attrs={'class': 'play-detail__accuracy'})]
    mods = [t.get('data-acronym') for t in topPlays.findAll('div', attrs={'class': 'mod'})]
    pp = [t.getText() for t in topPlays.findAll('div', attrs={'class': 'play-detail__pp'})]
    return plays


# Returns a player's rank given their id
def getPlayerRank(id):
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

    driver.get(f'https://osu.ppy.sh/users/{id}')

    content = driver.page_source
    soup = BeautifulSoup(content, features="html.parser")

    return int(soup.find('div', attrs={'class':'value-display__value'}).text[1:].replace(",", ""))


# Returns top plays of players within x ranks of a given player
def getPlays(id, x):
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

    playerRank = getPlayerRank(id)

    # Makes a list of all the players within two pages of the inputted player
    page_number = math.ceil(playerRank/50)
    if page_number == 1:
        driver.get("https://osu.ppy.sh/rankings/osu/performance?page=1#scores")
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")

        playerList = [p.get('data-user-id') for p in soup.findAll('a', attrs={'class': 'ranking-page-table__user-link-text js-usercard'})]
 
    else:
        driver.get(f"https://osu.ppy.sh/rankings/osu/performance?page={page_number-1}#scores")
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")

        playerList = [p.get('data-user-id') for p in soup.findAll('a', attrs={'class': 'ranking-page-table__user-link-text js-usercard'})]

        driver.get(f"https://osu.ppy.sh/rankings/osu/performance?page={page_number}#scores")
        content = driver.page_source
        soup = BeautifulSoup(content, features="html.parser")

        playerList += [p.get('data-user-id') for p in soup.findAll('a', attrs={'class': 'ranking-page-table__user-link-text js-usercard'})]

    # Filters the players to only provide those x ranks ahead
    if playerRank > 100:
        playerRank = playerRank - 50*(page_number-2)

    if playerRank-x < 1:
        playerListFiltered = playerList[0 : playerRank-1]
    else:
        playerListFiltered = playerList[playerRank-(x+1) : playerRank-1]
    
    # Returns the top plays of these x players

    plays = []
    for player in playerListFiltered:
        plays += getTopPlays(int(player))
    return plays



# Provides the farm maps for a given player
def main():
    plays = getPlays("oufoufouf", 3)
    print(plays)

if __name__ == "__main__":
    main()
