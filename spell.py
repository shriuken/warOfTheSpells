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
        """
        :return: Returns the name of the spell.
        """
        return self.spellName

    def get_efficiency(self, statsPackage, rank=0, targets=1):
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
                    # If rank > maxrank, set max rank as the current rank.
                    values[each['key']] = each['coeff'][self.maxRank]

                scaleType[each['key']] = each['link']

            if self.effect is not None:  # In case effect isn't returning properly. (*cough* Lux *cough*)
                #print 'split self.effect'
                for index in range(1, len(self.effect)):
                    if self.effect[index] is not None:
                        values['e' + str(index)] = self.effect[index][rank]

            # print 'finished splitting things up'

            #https://regex101.com/r/mF9dL8/16
            damageExpression = '(suffering|dealing|deals|deal|for|take|additional|takes) (?={{ [a-z])(?P<formula>.+?) (physical|magic|true|bonus) (?=damage)'

            #https://regex101.com/r/jW2vQ3/2
            healExpression = '(regaining|restores|offers|restoring|for) (?={{ [a-z])(?P<formula>.+?) (health)'

            # https://regex101.com/r/qS8gJ6/2
            keyExpression = '{{ ([a-z]\d) }}'  # Use this pattern when searching for e1, f1, etc.
            # https://regex101.com/r/sC7bI5/1
            operandExpression = '([\+\-])'
            # https://regex101.com/r/bV9uQ8/1
            activeExpression = '(Active:)'

            # Begin calculating the total damage the spell does in one 'tick'. Spells that do all their damage upfront,
            # such as Irelia's Bladesurge, do all their damage in one 'tick'. Where as Fiddlestick's Crowstorm deals all
            # of its damage in multiple ticks. Riven's Broken Wings would deal all its damage over the course of 3
            # ticks, since the spell can be activated up to 3 times sequentially. This calculation does not take into
            # account how many ticks occur over the entire duration of a spell; rather, this calculates the damage of
            # one 'tick'; thus spells that deal all their damage in one tick will return a higher efficiency.
            tickDamage = 0

            # print 'Splitting up tooltip to figure out formulas for damage.'

            try:
                # First, check to see if the spell has Passive/Active components. If they do, split by the Active, and
                # take the last entry of the split. Else, use the entirety of the tooltip.
                splitTip = ''

                #print re.split(activeExpression, self.sanitizedTooltip)

                if len(re.split(activeExpression, self.sanitizedTooltip)) > 1:
                    splitTip = re.split(activeExpression, self.sanitizedTooltip, 0, re.IGNORECASE)[-1]
                else:
                    splitTip = self.sanitizedTooltip

                # Gets damage formula. Assumes that the formula is in the tool tip following the regular expression
                # in the damage expression. Currently, this is extremely limiting.
                if re.search(damageExpression, splitTip, re.IGNORECASE) is not None:
                    formula = re.search(damageExpression, splitTip, re.IGNORECASE).group('formula')
                elif re.search(healExpression, splitTip, re.IGNORECASE) is not None:
                    formula = re.search(healExpression, splitTip, re.IGNORECASE).group('formula')
                # print formula

                splitFormula = re.split(operandExpression, formula, 0, re.IGNORECASE)

                # print splitFormula

                # Huge assumption; Assuming that the first element is always base damage (and thus has no scaling).
                tickDamage = values.get(re.search(keyExpression, splitFormula[0]).group(1))
                if tickDamage is None:
                    tickDamage = 0
                #print self.spellName, tickDamage, re.search(keyExpression, splitFormula[0]).group(1)

                # calculate damage of 1 tick.
                for x in range(1, len(splitFormula), 2):
                    # print splitFormula
                    if splitFormula[x] == '+':
                        token = re.search(keyExpression, splitFormula[x+1]).group(1)
                        #print token
                        #print values
                        #print scaleType
                        #print tickDamage
                        if values.get(token) is not None and scaleType.get(token) is not None:
                            tickDamage = tickDamage + values.get(token) * statsPackage.get(scaleType.get(token))
            except:
                #print "first exception."
                return -1.0

            # Now that we have total tick damage, calculate "efficiency" by dividing the amount of damage done in one
            # tick by the time it takes until, worst case scenario, the next tick of damage can be dealt. Again, this
            # methodology favors spells that deal all (or most) of their damage in the first tick.
            efficiency = tickDamage / (self.cooldown[rank] * (1 - statsPackage['cdr']))
            return efficiency
        except:
            #print "second exception."
            return -1.0
