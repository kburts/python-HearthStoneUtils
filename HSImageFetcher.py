import csv
import urllib


'''
Program to search through a .csv file and retrieve all of the images
    using urllib and save them to a file.
Can be modified to get other information about the cards.

Saves to images/ folder, which may need to me created.
'''


# Windows cannot use colons in their filenames, but linux can. Go linux!
# Set to false to replace all colons with ""(nothing).
USE_COLON = True

with open('Hearthstone_cards.csv', 'r') as csvcards:
    cards = csv.reader(csvcards)
    for row in cards:
        try:
            if ":" in row[1]:
                if USE_COLON == False:
                    print (row[1].replace(":", ""))
            else:
                pass
            urllib.urlretrieve(row[3], "images/%s.png" %row[1])
            print ("got %s" %row[1])
        except Exception:
            # This is required because the first row of the csv file is not a url
            print Exception

print "DONE! USE_COLON: %s." %USE_COLON

