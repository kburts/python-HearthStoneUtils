import csv
import urllib


'''
Program to search through a .csv file and retrieve all of the images
    using urllib and save them to a file.
Can be modified to get other information about the cards.

Saves to images/ folder, which may need to me created.
'''

with open('Hearthstone_cards.csv', 'r') as csvcards:
    cards = csv.reader(csvcards)
    for row in cards:
        #print row[3]
        try:
            urllib.urlretrieve(row[3], "images/"+row[1]+".png")
            print ("got %s" %row[1])
        except Exception:
            # This is required because the first row of the csv file is not a url
            print Exception

print "DONE!"
