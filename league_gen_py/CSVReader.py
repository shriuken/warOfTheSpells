import csv
import summoner as Summoner

__author__ = 'ryan'


with open('less_small_data.csv', 'rb') as inputFile:
    text = csv.reader(inputFile, delimiter=',')
    for row in text:
        # 0 is date/time stamp.
        # 1 is summoner name
        # 2 is primary lane
        # 3 - 6 is secondary lane
        newSummoner = Summoner()
        print row
        for each in row:
            newSummoner.
            print each
