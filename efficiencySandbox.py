__author__ = 'ryan'

import copy
import riot_api_wrapper.RiotAPI as API
import key as KEY
import spell as Spell

def main():

    api = API.RiotAPI(KEY.KEY)
    a = api.get_champion_list('spells')
    keys = []
    for pairs in a['data'].iteritems():
        keys.append(pairs[0])

    # Testing to write the code for Broken Wings.
    brokenWings = Spell.Spell()
    brokenWings.init_from_riot_api(a['data']['Riven']['spells'][0])
    # print type(a['data']['Riven']['spells'][0]['vars'])
    #print 'vars', a['data']['Riven']['spells'][0]['vars']
    #print type(a['data']['Riven']['spells'][0]['effect'])
    #print 'effect', a['data']['Riven']['spells'][0]['effect']
    #print type(a['data']['Riven']['spells'][0]['sanitizedTooltip'])
    print a['data']['Irelia']['spells'][0]['sanitizedTooltip']
    print a['data']['Riven']['spells'][0]['sanitizedTooltip']
    print a['data']['Veigar']['spells'][2]['sanitizedTooltip']
    print a['data']['MonkeyKing']['spells'][3]['sanitizedTooltip']
    #print a['data']['Riven']['spells'][0]['maxrank']
    #print a['data']['Riven']['spells'][0]['cooldown']

    brokenWings.get_efficiency()


main()