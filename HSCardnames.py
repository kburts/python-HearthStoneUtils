import csv
import json

'''
Program to search through a .csv file and retrieve all of the contents of
    one row, and save them to a json file.
can be modified to get other information about the cards.

File format: ["1","2","3"..."mystuff"].
'''

cardnames = []

with open('Hearthstone_cards.csv', 'r') as csvcards:
    cards = csv.reader(csvcards)
    for row in cards:
        cardnames.append(row[1])

with open('cardnames.json', 'w') as cardnames:
    cardnames.write(str(cardnames))
    
print "DONE!"
