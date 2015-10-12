__author__ = 'ryan'
# TODO:
# make league and division automatic when summoner name or ID is supplied.


class Summoner:
    def __init__(self):
        self.summonerName = ""
        self.summonerID = ""
        self.league = ""
        self.division = ""
        self.primaryRole = ""
        self.secondaryRole = ""

    def set_summoner_name(self, name):
        self.summonerName = name

    def set_summoner_id(self):
        self.summonerID = ""

    def set_league(self, league):
        self.league = league

    def set_division(self, division):
        self.division = division

    def set_primary_role(self, primaryRole):
        self.primaryRole = primaryRole

    def set_secondary_role(self, secondaryRole):
        self.secondaryRole = secondaryRole

    def get_summoner_name(self):
        return self.summonerName

    def get_summoner_id(self):
        return self.summonerID

    def get_league(self):
        return self.league

    def get_division(self):
        return self.division

    def get_primary_role(self):
        return self.primaryRole

    def get_secondary_role(self):
        return self.secondaryRole
