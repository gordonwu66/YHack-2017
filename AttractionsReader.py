'''
Created on Dec 1, 2017

@author: gordonwu
'''
from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd
import numpy as np

dataset = pd.read_csv("/Users/gordonwu/Downloads/LowestFares.csv") #Read in dataset
dMoney = dataset[dataset['FareType'] == 'LOWEST'] #Separates by FareType to only Money Based Fares
originMoney = np.array(dMoney['Origin'])
np.unique(originMoney)   #Finds all unique Origins
destinationMoney = np.array(dMoney['Destination'])
np.unique(destinationMoney)    #Finds all unique Destinations
temp = np.array(dMoney['FlightDate'])
settingMoney = temp.tolist()
dateMoney = [i.split(' ', 1)[0] for i in settingMoney] #Splits the FlightDate Column to just get the Date
uniqueDateMoney = []
for i in dateMoney:
    if i not in uniqueDateMoney: #Finds the unique dates of each of the flights
        uniqueDateMoney.append(i)


timeMoney = [i.split(' ', 1)[1] for i in settingMoney] #Splits the FlightDate Column to just get the Time
uniqueTimeMoney = []
for i in timeMoney:
    if i not in uniqueTimeMoney: #Finds the unique times of each of the flights
        uniqueTimeMoney.append(i)
sortedTimeMoney = sorted(uniqueTimeMoney)


amountMoney = np.array(dMoney['TotalAmount'])
sortedMoney = np.sort(amountMoney) #Sorts data set by the total cost of the flight, cheapest to most expensive


dPoints = dataset[dataset['FareType'] == 'POINTS'] #Separates by FareType to only Points Based Fares

originPoints = np.array(dPoints['Origin']) 
np.unique(originPoints)    #Finds all unique Origins

destinationPoints = np.array(dPoints['Destination'])
np.unique(destinationPoints)  #Finds all unique Destinations

temp1 = np.array(dPoints['FlightDate'])
settingPoints = temp1.tolist()
datePoints = [i.split(' ', 1)[0] for i in settingPoints] #Splits the FlightDate Column to just get the Date
uniqueDatePoints = []
for i in datePoints:
    if i not in uniqueDatePoints: #Finds the unique dates of each of the flights
        uniqueDatePoints.append(i)


timePoints = [i.split(' ', 1)[1] for i in settingPoints] #Splits the FlightDate Column to just get the Time
uniqueTimePoints = []
for i in timePoints:
    if i not in uniqueTimePoints: #Finds the unique times of each of the flights
        uniqueTimePoints.append(i)
sortedTimePoints = sorted(uniqueTimePoints)


amountPoints = np.array(dPoints['TotalAmount'])
sortedPoints = np.sort(amountPoints) #Sorts data set by the total cost of the flight, cheapest to most expensive

#creates a list of the bold keywords when searching top sights of the city
def attractionsFinder(userDestination):
    rootURL = 'http://www.google.com/search?q='
    city = userDestination
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
        

def findFlight():
    userOrigin = raw_input("Where are you leaving from?: ")
    
    userPossibleOrigins = dataset[dataset['Origin'] == userOrigin]
    destinationPoint = np.array(userPossibleOrigins['Destination'])
    print(np.unique(destinationPoint))
    userDestination = raw_input("Here are the available flight destinations. Where would you like to go?: ")
    print("Here are some buzzwords that show up through google search")
    attractionsFinder(userDestination)
    
findFlight()
    
