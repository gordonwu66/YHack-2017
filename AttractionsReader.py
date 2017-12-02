'''
Created on Dec 1, 2017

@author: gordonwu
'''
from bs4 import BeautifulSoup
import requests

#creates a list of the bold keywords when searching top sights of the city
def attractionsFinder():
    rootURL = 'http://www.google.com/search?q='
    city = raw_input('Enter a city: ')
    cityURL = city.replace(" ", "+")

    finalURL = rootURL + cityURL + "+top+sights"

    page = requests.get(finalURL)
    soup = BeautifulSoup(page.text, 'html.parser')

    keyWords = soup.find_all('b')

    length = len(keyWords)
    
    #formatting
    for i in range(length):
        keyWords[i] = str(keyWords[i]).replace('<b>', '')
        keyWords[i] = keyWords[i].replace('</b>', '')
        keyWords[i] = keyWords[i].replace('<b class="gb1">', '')
    
    deleteRepeats(keyWords)

#removes all repeated elements
def deleteRepeats(keyWords):
    uniqueKeyWords = []
    for i in keyWords:
        if i not in uniqueKeyWords:
            uniqueKeyWords.append(i)
    
    for i in range(len(uniqueKeyWords)):
        print(uniqueKeyWords[i])
        
attractionsFinder()
