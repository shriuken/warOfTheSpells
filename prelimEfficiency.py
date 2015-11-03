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
    spellData = api.get_champion_list('spells')
    keys = []

    for pairs in spellData['data'].iteritems():
        keys.append(pairs[0])

    stats = create_basic_stats_package(keys, spellData['data'])

    mostEfficientName = ""
    mostEfficientValu = -1.0

    for champ in keys:
        for x in range(0, 4):
            spell = Spell.Spell()
            spell.init_from_riot_api(spellData['data'][champ]['spells'][x])
            if spell.get_efficiency(stats) is not None:
                if spell.get_efficiency(stats) > mostEfficientValu:
                    mostEfficientName = spell.get_name()
                    mostEfficientValu = spell.get_efficiency(stats)

    print mostEfficientName, mostEfficientValu
    # print spellData['data']['Rengar']['spells'][2]
    print 'cooldown', spellData['data']['Rengar']['spells'][2]['cooldown']
    print 'effect', spellData['data']['Rengar']['spells'][2]['effect']
    print 'vars', spellData['data']['Rengar']['spells'][2]['vars']
    print 'sanitized', spellData['data']['Rengar']['spells'][2]['sanitizedTooltip']


main()
