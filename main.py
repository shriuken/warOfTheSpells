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
        #if champ == "Rengar" or champ == "Rumble" or champ == "Vi":
        #    continue
        for x in range(0, 4):
            currentSpell = Spell.Spell()
            currentSpell.init_from_riot_api(spellData['data'][champ]['spells'][x])
            spellEfficiency = currentSpell.get_efficiency(stats)
            if spellEfficiency is not None and spellEfficiency > ret[1]:
                ret[0] = currentSpell.get_name()
                ret[1] = spellEfficiency
    return ret


def create_stats(ad, ap, cdr, armor, health):
    """
    :param ad: The value of AD to assign. This is assigned to both attack damage and bonus attack damage.
    :param ap: The value of AP to assign. This is assigned to just spell damage.
    :param cdr: The value of cool down reduction to assign.
    :return:
    """
    ret = {'attackdamage': ad, 'bonusattackdamage': ad, 'spelldamage': ap, 'armor': armor, 'bonusarmor': armor,
           'health': health, 'cdr': cdr}
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
    for health in range(0, 4001, 500):
        for ap in range(0, 801, 100):
            for ad in range(0, 401, 50):
                for armor in range(0, 201, 50):
                    for cdr in range(0, 41, 5):
                        stats = create_stats(ad, ap, cdr * 0.01, armor, health)
                        best = get_most_efficient(spellData, stats, keys)
                        print best[0], 'is the most efficient spell at', health, 'health', ', armor', armor, ', AD', ad, ', AP', ap, ', CDR', cdr, '%. The efficiency coefficient is: ', best[1], '.'
                        if bestCount.get(best[0]) is None:
                            bestCount[best[0]] = 1
                        else:
                            bestCount[best[0]] += 1
    print ''
    print ''
    for pair in bestCount:
        print pair

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
