import csv
import key
import riot_api_wrapper.RiotAPI as API
import summoner as Summoner

__author__ = 'ryan'


api = API.RiotAPI(key.KEY)
with open('less_small_data.csv', 'rb') as inputFile:
    text = csv.reader(inputFile, delimiter=',')
    pastFirstLine = False
    summonerNames = []
    summonerPrimaryLanes = {}
    summonerSecondaryLanes = {}
    for row in text:
        # 0 is date/time stamp.
        # 1 is summoner name
        # 2 is primary lane
        # 3 - 6 is secondary lane
        if not pastFirstLine:
            pastFirstLine = True
        else:
            summonerNames.append(row[1] + ', ')
            summonerPrimaryLanes.update({row[1]: row[2]})
            for x in range(3, 7):
                if row[x] != "":
                    summonerSecondaryLanes.update({row[1]: row[x]})
    summoners = api.get_summoner_by_names("".join(summonerNames))
        #if validSummoner != 'error':
        #    newSummoner = Summoner()
        #    print validSummoner
