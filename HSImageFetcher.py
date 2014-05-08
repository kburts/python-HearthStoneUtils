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
        try:
            if ":" in row[1]:
                # You cannot save files with colins in them, so they
                #   must be removed!
                print (row[1].replace(":", ""))
            else:
                pass
            urllib.urlretrieve(row[3], "images/%s.png" %row[1])
            print ("got %s" %row[1])
        except Exception:
            # This is required because the first row of the csv file is not a url
            print Exception

print "DONE!"

