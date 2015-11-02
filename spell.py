__author__ = 'shriuken154'
import re

class Spell:
    def __init__(self):
        """
        Initial constructor for spell class. Initializes everything to None.
        :return: None
        """
        self.spellName = None
        self.vars = None
        self.costType = None
        self.cost = None
        self.sanitizedTooltip = None
        self.effect = None
        self.maxRank = None

    def init_from_riot_api(self, spellData):
        """
        :param spellData: The spell dictionary from Riot's API
        :return: None
        """
        # ['data']['Shaco']['spells'][0].get('vars')
        self.spellName = spellData.get('name')
        self.vars = spellData.get('vars')
        self.costType = spellData.get('costType')  # Might need to complicate the assignment slightly to clean up { }
        self.cost = spellData.get('cost')  # might change based on cost type
        self.sanitizedTooltip = spellData.get('sanitizedTooltip')  # Contains relations for damages.
        self.effect = spellData.get('effect')
        self.maxRank = spellData.get('maxrank')

    def get_efficiency(self, statsPackage = {}, rank = 0, targets = 1):
        """
        Calculates the efficiency of a spell.
        :param targets: The number of targets the spell is hitting.
        :param rank: The rank of the spell. Zero based (rank 1 is 0)
        :param statsPackage: The dictionary containing stats to test efficiency.
        :return: Returns the efficiency of the spell. The efficiency is calculated as total damage / cool down.
        """
        # Generate a dictionary of appropriate values.
        values = {}
        # Get coefficients. This is a terrible way to do it though.
        for each in self.vars:
            values[each['key']] = []
            values[each['key']].append(each['coeff'][rank])
            values[each['key']].append(each['link'])

        for index in range(1, len(self.effect)):
            values['e' + str(index)] = self.effect[index][rank]

        damageFormula = re.search('dealing (.*) physical|magic|true|bonus', self.sanitizedTooltip)
        print damageFormula.group(0)

        print values

