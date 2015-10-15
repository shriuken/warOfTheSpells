import requests

import RiotConstants as Consts

__author__ = 'ryan'
# following tutorial https://www.youtube.com/watch?v=0NycEiHOeX8


class RiotAPI:
    def __init__(self, api_key, region=Consts.REGIONS['north_america']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params={}):
        """
        :param api_url: the http command to execute
        :param params:
        :return: the json response of the http command. OR 'error' if not found.
        """
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(
                proxy=self.region,
                region=self.region,
                url=api_url
            ),
            params=args
        )
        # probably should check for status codes here.
        if response.status_code == 200:
            return response.json()
        else:
            return 'error'

    def get_champions(self):
        api_url = Consts.URL['champions'].format(
            version=Consts.API_VERSIONS['champion']
        )
        return self._request(api_url)

    def get_champion_by_id(self, champ_id):
        api_url = Consts.URL['champion_by_id_champion'].format(
            version=Consts.API_VERSIONS['champion'],
            id=champ_id
        )
        return self._request(api_url)

    def get_current_game(self, platform, summoner_id):
        api_url = Consts.URL['current_game'].format(
            platformId=platform,
            summonerId=summoner_id
        )
        return self._request(api_url)

    def get_featured_games(self):
        api_url = Consts.URL['featured_games']
        return self._request(api_url)

    def get_recent_games_by_summoner_id(self, summoner_id):
        api_url = Consts.URL['recent_games_by_summoner_id'].format(
            version=Consts.URL['game'],
            summonerId=summoner_id
        )
        return self._request(api_url)

    def get_leagues_by_summoner_ids(self, summoner_ids):
        api_url = Consts.URL['leagues_by_summoner_ids'].format(
            version=Consts.URL['league'],
            summonerIds=summoner_ids
        )
        return self._request(api_url)

    def get_league_entries_by_summoner_ids(self, summoner_ids):
        api_url = Consts.URL['league_entries_by_summoner_ids'].format(
            version=Consts.API_VERSIONS['league'],
            summonerIds=summoner_ids
        )
        return self._request(api_url)

    def get_leagues_by_team_ids(self, team_ids):
        api_url = Consts.URL['leagues_by_team_ids'].format(
            version=Consts.API_VERSIONS['league'],
            teamIds=team_ids
        )
        return self._request(api_url)

    def get_league_entries_by_team_ids(self, team_ids):
        api_url = Consts.URL['league_entries_by_team_ids'].format(
            version=Consts.API_VERSIONS['league'],
            teamIds=team_ids
        )
        return self._request(api_url)

    def get_challenger(self):
        api_url = Consts.URL['challenger'].format(
            version=Consts.API_VERSIONS['league']
        )
        return self._request(api_url)

    def get_master(self):
        api_url = Consts.URL['master'].format(
            version=Consts.API_VERSIONS['league']
        )
        return self._request(api_url)

    #  LoL static-data is currently not implemented/supported.

    def get_shards(self):
        api_url = Consts.URL['shards']
        return self._request(api_url)

    def get_shard_status(self, shard_region):
        api_url = Consts.URL['shard_status'].format(
            region=shard_region
        )
        return self._request(api_url)

    def get_match_by_match_id(self, match_id):
        api_url = Consts.URL['match_by_match_id'].format(
            version=Consts.API_VERSIONS['match'],
            matchId=match_id
        )
        return self._request(api_url)

    def get_match_list_by_summoner_id(self, summoner_id):
        api_url = Consts.URL['match_list_by_summoner_id'].format(
            version=Consts.API_VERSIONS['matchlist'],
            summonerId=summoner_id
        )
        return self._request(api_url)

    def get_ranked_stats_by_id(self, summoner_id):
        api_url = Consts.URL['ranked_stats_by_id'].format(
            version=Consts.API_VERSIONS['stats'],
            summonerId=summoner_id
        )
        return self._request(api_url)

    def get_stats_summary_by_id(self, summoner_id):
        api_url = Consts.URL['get_stats_summary_by_id'].format(
            version=Consts.API_VERSIONS['stats'],
            summonerId=summoner_id
        )
        return self._request(api_url)

    def get_summoner_by_names(self, summoner_names):
        api_url = Consts.URL['summoner_by_names'].format(
            version=Consts.API_VERSIONS['summoner'],
            names=summoner_names
        )
        return self._request(api_url)

    def get_summoner_by_ids(self, summoner_ids):
        api_url = Consts.URL['summoner_by_ids'].format(
            version=Consts.API_VERSIONS['summoner'],
            summonerIds=summoner_ids
        )
        return self._request(api_url)

    def get_summoner_masteries(self, summoner_ids):
        api_url = Consts.URL['summoner_masteries'].format(
            version=Consts.API_VERSIONS['summoner'],
            summonerIds=summoner_ids
        )
        return self._request(api_url)

    def get_summoner_names_by_ids(self, summoner_ids):
        api_url = Consts.URL['summoner_names_by_ids'].format(
            version=Consts.API_VERSIONS['summoner'],
            summonerIds=summoner_ids
        )
        return self._request(api_url)

    def get_summoner_runes(self, summoner_ids):
        api_url = Consts.URL['summoner_runes'].format(
            version=Consts.URL['summoner'],
            summonerIds=summoner_ids
        )
        return self._request(api_url)

    def get_team_by_summoner_ids(self, summoner_ids):
        api_url = Consts.URL['team_by_summoner_ids'].format(
            version=Consts.URL['team'],
            summonerIds=summoner_ids
        )
        return self._request(api_url)

    def get_team_by_team_ids(self, team_ids):
        api_url = Consts.URL['team_by_team_ids'].format(
            version=Consts.URL['team'],
            teamIds=team_ids
        )
        return self._request(api_url)