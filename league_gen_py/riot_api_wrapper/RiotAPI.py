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
        :return: the json response of the http command.
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
        print response.url
        return response.json()

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

    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
            version=Consts.API_VERSIONS['summoner'],
            names=name
        )
        return self._request(api_url)
