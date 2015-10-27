__author__ = 'ryan'
import riot_api_wrapper.RiotAPI as API
import key as KEY

api = API.RiotAPI(KEY.KEY)
a = api.get_champion_list('spells')
# a = api.get_champion_list()
# print type(a['data']['MonkeyKing'])
# print a['data']['Leblanc']
x = 0
keys = []
for key in a['data'].iteritems():
    keys.append(key)
    x = x+1
# print(api.get_champion_list('spells'))
print len(keys)
y = 0
for key, value in keys:
    print value['spells'][1]['key']
    y+=1

