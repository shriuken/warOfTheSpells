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
    ret = ['', -1]
    for champ in spellDataKeys:
        if champ == "Rengar" or champ == "Rumble" or champ == "Vi":
            continue
        for x in range(0, 4):
            currentSpell = Spell.Spell()
            currentSpell.init_from_riot_api(spellData['data'][champ]['spells'][x])
            if currentSpell.get_efficiency(stats) is not None:
                if currentSpell.get_efficiency(stats) > ret[1]:
                    ret[0] = currentSpell.get_name()
                    ret[1] = currentSpell.get_efficiency(stats)
    return ret


def create_zero_stats_package(champions, dataDict):
    """
    Creates a stats dictionary with each stat assigned to 0.
    :param champions: The list of champions in dataDict.
    :param dataDict: The spell dictionary.
    """
    stats = {}
    for champ in champions:
        for x in range(0, 4):
            if dataDict[champ]['spells'][x].get('vars') is not None:
                for sublist in dataDict[champ]['spells'][x]['vars']:
                    if sublist['link'][0] != '@' and sublist['link'][0] != '.':
                        stats[sublist['link']] = 0
    stats['cdr'] = 0.0
    return stats


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


def modify_stats_package(stats, stat, value):
    """
    :param stats: The statsPackage dictionary to modify values in.
    :param stat: The stat you wish to change.
    :param value: The value to change the stat to.
    """
    #  bonusSTAT is treated the same as STAT
    if stat is 'health' or stats is 'bonushealth':
        stats['health'] += value
        stats['bonushealth'] += value
    elif stat is 'armor' or stat is 'bonusarmor':
        stats['armor'] += value
        stats['bonusarmor'] += value
    elif stat is 'attackdamage' or stat is 'bonusattackdamage':
        stats['attackdamage'] += value
        stats['bonusattackdamage'] += value
    # Assuming valid input supplied is not bonusSTAT.
    elif stat is 'cdr' and stats['cdr'] + value > .40:
        stats['cdr'] = .40
    else:
        stats[stat] += value
    return stats


def evaluate_only_ad(keys, spellData, rank=0):
    """
    :param keys: The list of keys to the spellData dictionary.
    :param spellData: The dictionary of spell data.
    :param rank: The rank of spell to evaluate.
    """
    print "Evaluating most efficient spell at varying levels of attack damage and spell rank 1."
    stats = create_zero_stats_package(keys, spellData['data'])
    # storing some data in a list, this is bad but it's a hack and yay python.
    oldBest = ['', -1]
    for x in range(0, 500):
        newBest = get_most_efficient(spellData, stats, keys)
        if newBest[0] != oldBest[0]:
            if newBest[1] > oldBest[1]:
                oldBest[0] = newBest[0]
                oldBest[1] = newBest[1]
                print "At ", stats['attackdamage'], " AD ", newBest[0], " becomes the best spell with an efficiency coeff of ", newBest[1]
        stats['attackdamage'] = x
        stats['bonusattackdamage'] = x
    print "===== End Pure AD Evaluation. Total Range of Evaluation: 0 to 500 AD ====="
    print ''


def evaluate_only_ap(keys, spellData, rank=0):
    """
    :param keys: The list of keys to the spellData dictionary.
    :param spellData: The dictionary of spell data.
    :param rank: The rank of spell to evaluate.
    """
    print "Evaluating most efficient spell at varying levels of spell power and spell rank 1."
    stats = create_zero_stats_package(keys, spellData['data'])
    # storing some data in a list, this is bad but it's a hack and yay python.
    oldBest = ['', -1]
    for x in range(0, 500):
        newBest = get_most_efficient(spellData, stats, keys)
        if newBest[0] != oldBest[0]:
            if newBest[1] > oldBest[1]:
                oldBest[0] = newBest[0]
                oldBest[1] = newBest[1]
                print "At ", stats['spelldamage'], " AP ", newBest[0], " becomes the best spell with an efficiency coeff of ", newBest[1]
        stats['spelldamage'] = x
    print "===== End Pure AP Evaluation. Total Range of Evaluation: 0 to 500 AP ====="
    print ''


def evaluate_only_cdr(keys, spellData, rank=0):
    """
    :param keys: The list of keys to the spellData dictionary.
    :param spellData: The dictionary of spell data.
    :param rank: The rank of spell to evaluate.
    """
    print "Evaluating most efficient spell at varying levels of attack damage and spell rank 1."
    stats = create_zero_stats_package(keys, spellData['data'])
    # storing some data in a list, this is bad but it's a hack and yay python.
    oldBest = ['', -1]
    for x in range(0, 41):
        newBest = get_most_efficient(spellData, stats, keys)
        if newBest[0] != oldBest[0]:
            if newBest[1] > oldBest[1]:
                oldBest[0] = newBest[0]
                oldBest[1] = newBest[1]
                print "At ", stats['cdr'], " CDR ", newBest[0], " becomes the best spell with an efficiency coeff of ", newBest[1]
        stats['cdr'] = x * 0.001
    print "===== End Pure CDR Evaluation. Total Range of Evaluation: 0 to 40% CDR ====="
    print ''


def createStats(ad, ap, cdr):
    """
    :param ad: The value of AD to assign. This is assigned to both attack damage and bonus attack damage.
    :param ap: The value of AP to assign. This is assigned to just spell damage.
    :param cdr: The value of cool down reduction to assign.
    :return:
    """
    ret = {'attackdamage': ad, 'bonusattackdamage': ad, 'spelldamage': ap, 'cdr': cdr}
    return ret


def mixed_evaluation(keys, spellData, rank=0):
    """
    Calculates the most efficient spell for every combination of AD from 0 to 500, AP from 0 to 800, and CDR from 0% to
    40%. It then prints this out to screen. VERY SLOW. Should probably run from command line to speed up. Don't just
    call willy-nilly.
    :param keys: the list of champ names to use.
    :param spellData: the data dictionary
    :param rank: the spell rank to evaluate.
    """
    bestCount = {}
    for ad in range(0, 501):
        for ap in range(0, 801):
            for cdr in range(0, 41):
                stats = createStats(ad, ap, cdr * .01)
                newBest = get_most_efficient(spellData, stats, keys)
                # print newBest[0], 'and', oldBest[0]
                print "At ", ad, " AD, ", ap, " AP, and ", cdr, "% CDR, ", newBest[0], " is the most efficient spell with an efficiency coeff of ", newBest[1]
                if bestCount.get(newBest[0]) is None:
                    bestCount[newBest[0]] = 1
                else:
                    bestCount[newBest[0]] += 1
    print ''
    print ''
    for pair in bestCount:
        print pair[0], ':', pair[1]


def main():
    """
    The main entry point of the program.
    """
    api = API.RiotAPI(KEY.KEY)
    spellData = api.get_champion_list('spells')
    keys = []

    for pairs in spellData['data'].iteritems():
        keys.append(pairs[0])

    mixed_evaluation(keys, spellData)


main()
