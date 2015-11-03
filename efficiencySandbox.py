__author__ = 'ryan'

import copy
import riot_api_wrapper.RiotAPI as API
import key as KEY
import spell as Spell


def create_basic_stats_package(champions, dataDict):
    stats = {}
    for champ in champions:
        for x in range(0, 4):
            if dataDict[champ]['spells'][x].get('vars') is not None:
                for sublist in dataDict[champ]['spells'][x]['vars']:
                    if sublist['link'][0] != '@' and sublist['link'][0] != '.':
                        stats[sublist['link']] = 100
    stats['cdr'] = 0.10
    return stats


def main():
    api = API.RiotAPI(KEY.KEY)
    a = api.get_champion_list('spells')
    keys = []
    for pairs in a['data'].iteritems():
        keys.append(pairs[0])

    stats = create_basic_stats_package(keys, a['data'])

    # Testing to write the code for Broken Wings.
    brokenWings = Spell.Spell()
    brokenWings.init_from_riot_api(a['data']['Riven']['spells'][0])
    # print type(a['data']['Riven']['spells'][0]['vars'])
    """print 'vars', a['data']['Riven']['spells'][0]['vars']
    print type(a['data']['Riven']['spells'][0]['effect'])
    print 'effect', a['data']['Riven']['spells'][0]['effect']
    print type(a['data']['Riven']['spells'][0]['sanitizedTooltip'])"""
    """print a['data']['Irelia']['spells'][0]['sanitizedTooltip']
    print a['data']['Riven']['spells'][0]['sanitizedTooltip']
    print a['data']['Veigar']['spells'][2]['sanitizedTooltip']
    print a['data']['MonkeyKing']['spells'][3]['sanitizedTooltip']
    print a['data']['Riven']['spells'][0]['maxrank']
    print a['data']['Riven']['spells'][0]['cooldown']"""
    # print a['data']['Nasus']['spells'][0]

    print brokenWings.get_efficiency(stats)

main()
