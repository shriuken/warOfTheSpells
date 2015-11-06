__author__ = 'ryan'

import riot_api_wrapper.RiotAPI as API
import key as KEY
import spell as Spell

def get_most_efficient(spellData, stats, spellDataKeys):
    """
    Returns the most efficient spell for a given stat dictionary.
    :param spellData: The dictionary of spell data.
    :param stats: Stat package to evaluate the most efficient spell at.
    :param spellDataKeys: The list of keys to the spell data dictionary.
    """
    ret = ['', -1, [], [], {}, [], []]
    for champ in spellDataKeys:
        #if champ == "Rengar" or champ == "Rumble" or champ == "Vi":
        #    continue
        for x in range(0, 4):
            currentSpell = Spell.Spell()
            currentSpell.init_from_riot_api(spellData['data'][champ]['spells'][x])
            if currentSpell.get_efficiency(stats) > 0:
                ret[4][currentSpell.get_name()] = currentSpell.get_efficiency(stats)
                ret[5].append(champ)
                ret[2].append(currentSpell.get_name())
                if currentSpell.get_efficiency(stats) > ret[1]:
                    ret[0] = currentSpell.get_name()
                    ret[1] = currentSpell.get_efficiency(stats)
            else:
                ret[3].append(currentSpell.get_name())
                ret[6].append(champ)
    return ret


def create_basic_stats_package(champions, dataDict):
    """
    Creates a stats dictionary with arbitrarily assigned magic numbers.
    :param champions: The list of champions in dataDict.
    :param dataDict: The spell dictionary.
    """
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
    """
    The main entry point of the program.
    """
    api = API.RiotAPI(KEY.KEY)
    spellData = api.get_champion_list('spells')
    keys = []

    for pairs in spellData['data'].iteritems():
        keys.append(pairs[0])

    stats = create_basic_stats_package(keys, spellData['data'])

    currentSpell = Spell.Spell()
    currentSpell.init_from_riot_api(spellData['data']['Jax']['spells'][3])
    #print currentSpell.get_efficiency(stats)


    ret = get_most_efficient(spellData, stats, keys)
    #print 'calculated:', ret[2]
    print 'total calculated:', len(ret[2])
    #print ret[5]
    #print 'not calculated:', ret[3]
    for each in ret[3]:
        print each
    print 'total not calculated:', len(ret[3])
    # print ret[4]
    lastPrint = ''
    x = 0
    #for each in ret[6]:
    #    print each
    #print ret[6]


main()
