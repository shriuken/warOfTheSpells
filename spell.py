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
        self.cooldown = None
        self.effect = None
        self.maxRank = None

    def init_from_riot_api(self, spellData):
        """
        :param spellData: The spell dictionary from Riot's API
        :return: None
        """
        self.spellName = spellData.get('name')
        self.vars = spellData.get('vars')
        self.costType = spellData.get('costType')  # Might need to complicate the assignment slightly to clean up { }
        self.cost = spellData.get('cost')  # might change based on cost type
        self.sanitizedTooltip = spellData.get('sanitizedTooltip')  # Contains relations for damages.
        self.cooldown = spellData.get('cooldown')
        self.effect = spellData.get('effect')
        self.maxRank = spellData.get('maxrank')

    def get_name(self):
        return self.spellName

    def get_efficiency(self, statsPackage={}, rank=0, targets=1):
        """
        Calculates the efficiency of a spell.
        :param targets: The number of targets the spell is hitting.
        :param rank: The rank of the spell. Zero based (rank 1 is 0)
        :param statsPackage: The dictionary containing stats to test efficiency.
        :return: Returns the efficiency of the spell. The efficiency is calculated as total damage / cool down.
        """
        # Generate a dictionary of appropriate values.
        values = {}
        scaleType = {}
        # Get coefficients and scaling.
        try:
            for each in self.vars:
                if self.maxRank > rank:
                    values[each['key']] = each['coeff'][rank]
                else:
                    values[each['key']] = each['coeff'][0]

                scaleType[each['key']] = each['link']

            for index in range(1, len(self.effect)):
                values['e' + str(index)] = self.effect[index][rank]

            # https://regex101.com/r/mF9dL8/4
            damageExpression = '(dealing|suffering|deal) (?P<formula>.+?) (physical|magic|true|bonus)'
            # https://regex101.com/r/qS8gJ6/2
            keyExpression = '{{ ([a-z]\d) }}'  # Use this pattern when searching for e1, f1, etc.
            # https://regex101.com/r/sC7bI5/1
            operandExpression = '([\+\-])'

            # Begin calculating the total damage the spell does in one 'tick'. Spells that do all their damage upfront,
            # such as Irelia's Bladesurge, do all their damage in one 'tick'. Where as Fiddlestick's Crowstorm deals all
            # of its damage in multiple ticks. Riven's Broken Wings would deal all its damage over the course of 3 ticks,
            # since the spell can be activated up to 3 times sequentially. This calculation does not take into account how
            # many ticks occur over the entire duration of a spell; rather, this calculates the damage of one 'tick'; thus
            # spells that deal all their damage in one tick will return a higher efficiency.

            tickDamage = 0

            try:
                # Gets damage formula. Assumes that the formula is in the tool tip following the regular expression
                # in the damage expression. Currently, this is extremely limiting.
                formula = re.search(damageExpression, self.sanitizedTooltip).group('formula')
                splitFormula = re.split(operandExpression, formula)

                # Huge assumption; Assuming that the first element is always base damage (and thus has no scaling).
                tickDamage = values.get(re.search(keyExpression, splitFormula[0]).group(1))

                # calculate damage of 1 tick.
                for x in range(1, len(splitFormula), 2):
                    if splitFormula[x] == '+':
                        token = re.search(keyExpression, splitFormula[x+1]).group(1)
                        if scaleType.get(token) is not None and scaleType.get(token) is not None:
                            tickDamage = tickDamage + values.get(token) * statsPackage.get(scaleType.get(token))
                        #else:
                            #totalDamage = totalDamage + values.get(token)
            except:
                return -1.0

            # Now that we have total tick damage, calculate "efficiency" by dividing the amount of damage done in one tick
            # by the time it takes until, worst case scenario, the next tick of damage can be dealt. Again, this methodology
            # favors spells that deal all (or most) of their damage in the first tick.
            efficiency = tickDamage / (self.cooldown[rank] * (1 - statsPackage['cdr']))
            return efficiency
        except:
            return -1.0
