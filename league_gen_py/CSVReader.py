import csv
import key
import riot_api_wrapper.RiotAPI as API
import summoner as Summoner

__author__ = 'ryan'


api = API.RiotAPI(key.KEY)
with open('less_small_data.csv', 'rb') as inputFile:
    text = csv.reader(inputFile, delimiter=',')
    for row in text:
        # 0 is date/time stamp.
        # 1 is summoner name
        # 2 is primary lane
        # 3 - 6 is secondary lane

        # TODO: read up more on the csv.reader return object.
        print row[1]
        validSummoner = api.get_summoner_by_names(row[1])
        #if validSummoner != 'error':
        #    newSummoner = Summoner()
        #    print validSummoner
