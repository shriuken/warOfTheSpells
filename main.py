from riot_api_wrapper import RiotAPI as RiotAPI
import key as key

__author__ = 'ryan'


def main():
    api = RiotAPI.RiotAPI(key.KEY)
    # r = api.get_summoner_by_name('shriuken154')
    # r = api.get_champion_by_id(266)
    r = api.get_champion_by_id('266')
    print r


if __name__ == "__main__":
    main()
