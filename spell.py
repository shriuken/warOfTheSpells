__author__ = 'shriuken154'

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
        :param dict: The spell dictionary from Riot's API
        :return: None
        """
        self.spellName = spellData['name']
        self.vars = spellData['vars']
        self.costType = spellData['costType']  # Might need to complicate the assignment slightly to clean up { }
        self.cost = spellData['cost']  # might change based on cost type
        self.sanitizedTooltip = spellData['sanitizedTooltip']  # Contains relations for damages.
        self.effect = spellData['effect']
        self.maxRank = spellData['maxrank']
