# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:12:51 2019

@author: tlf719
"""
from math import pi

# function for volume of block with hole
def volHoleyBlock(length, width, height, radius):
    ''' Function returns a negative value if passed parameter data is invalid.'''
    # check for valid data
    # not the best way to do this
    # this is minimal check at best
    if length <=0 or width <= 0 or height <= 0 or radius <= 0 or \
       radius >= min(length, width):
        return -1
    else:
        # assume consistent units for all terms
        origVol = length * width * height
        # hole is along height
        volHole = pi * radius * radius * height
        # subtract hole volume from original
        remainVol = origVol - volHole
        # return the remaining volume
        return remainVol
# end volHoleyBlock

# function for least profitable facility
def leastProfit(facilities, annualCost, valueProduct ):
    # get length of the lists - assume all are of equal length
    lenLists = len(facilities)
    
    # loop through the lists, find minimum of value - cost
    indMin = 0
    minProfit = valueProduct[0] - annualCost[0]
    for i in range(1, lenLists):
        if (valueProduct[i] - annualCost[i]) < minProfit:
            indMin = i
    # return name of facility with least profitibility + profitibility
    return facilities[indMin], (valueProduct[indMin] - annualCost[indMin])
# end leastProfit
    
# function for printing mail label
def printLabel(name, address1, address2,city, state, zipCode):
    print(name)
    print(address1)
    if address2 != '':
        print(address2)
    print(city + ', ' + state + '  ' + zipCode)
# end printLabel
# function for printing mail label
 
def printLabel_alt(name, addressList,city, state, zipCode):
    print(name)
    for item in addressList:
        print(item)
    print(city + ', ' + state + '  ' + zipCode)
# end printLabel_alt

# function for changing CSV to tab separated file
def CSVtoTab(filename):
    # open the CSV file for reading
    # open the tab file for writing
    FIDR = open(filename, 'r')
    FIDW = open('tabSepFile.tsv', 'w')
    
    for nextLine in FIDR:
        listStr = nextLine.split(',')
        for i in range(len(listStr)-1):  # loop doesn't use last item
            FIDW.write(listStr[i]+'\t')
        FIDW.write(listStr[-1]) # should still have '\n'
        
    FIDR.close()
    FIDW.close()
# end CSVtoTav
     
# function for max, min, mean of list
def listStats(listName):
    sumTot = 0.
    for item in listName:
        sumTot += item
    mean = sumTot / len(listName)
    maxValue = max(listName)
    minValue = min(listName)
    
    return mean, maxValue, minValue
# end listStats

# function for average velocities from two list
def avgVel(distList, timeList):
    # no error checking
    lenLists = len(distList)
    avgVelList = []
    for i in range(1, lenLists):
        avgVelList.append((distList[i] - distList[i-1])/(timeList[i] - timeList[i-1]))
    return avgVelList
# end avgVel
        
    
# begin main program

# test volHoleyBlock
length = 1
width = 1
height =1
radius = 1

volume = volHoleyBlock(length, width, height, radius)
print('volume = %f cubic units' % volume)
print()

# test leastProfit
facilities = ['AAAAA', 'BBBBB', 'CCCCC', 'DDDDD', 'EEEEE']
cost = [12.3, 14.2, 9.7, 18.2, 15.0]
value = [14.5, 17.2, 13.7, 25.2, 18.4]
a, b = leastProfit(facilities, cost, value)
print('Facility %s is least profitible.' % a)
print('Net profit for that facility is %f million dollars.' % b)
print()

# test printLabel
name = 'Edward Q. Public'
address1 = '3434 Plaza Court'
address2 = ''
city = 'Houston'
state = 'TX'
zipCode = '77076'

printLabel(name, address1, address2,city, state, zipCode)
print()

# test printLabel_alt
name = 'Edward Q. Public'
addressList = ['3434 Plaza Court', 'Suite 6754-B']
city = 'Houston'
state = 'TX'
zipCode = '77076'

printLabel_alt(name, addressList,city, state, zipCode)
print()

# test CSVtoTab
CSVtoTab('DataForCSV.csv')

# test listStats
myList = [1, 2, -2, 4, 5]
mean, max, min = listStats(myList)
print('mean = %f' % mean)
print('max = %f' % max)
print('min = %f' % min)
print()

# test avgVel
dList = [0, 1, 4, 9, 16]
tList = [0, 1, 2, 3, 4]
averageVel = avgVel(dList, tList)
print('list of average velocities = ', averageVel)


