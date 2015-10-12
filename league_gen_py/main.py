from leagueTeamGenerator.league_gen_py.riot_api_wrapper import RiotAPI
from leagueTeamGenerator.league_gen_py import key

__author__ = 'ryan'


def main():
    api = RiotAPI(key.KEY)
    r = api.get_summoner_by_name('shriuken154')
    print r


if __name__ == "__main__":
    main()
