__author__ = 'ryan'
# followed tutorial https://www.youtube.com/watch?v=0NycEiHOeX8

URL = {
    'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
    'summoner_by_name': 'v{version}/summoner/by-name/{names}'
}

API_VERSIONS = {
    # these versions are the versions used when call to Riot is made
    'champion': '1.2',
    'current-game': '1.0',
    'featured-games': '1.0',
    'game': '1.3',
    'league': '2.5',
    'lol-static-data': '1.2',
    'lol-status': '1.0',
    'match': '2.2',
    'matchlist': '2.2',
    'stats': '1.3',
    'summoner': '1.4',
    'team': '2.4'

}

REGIONS = {
    'brazil': 'br',
    'europe_nordic_and_east': 'eune',
    'europe_west': 'euw',
    'korea': 'kr',
    'latin_america_north': 'lan',
    'latin_america_south': 'las',
    'north_america': 'na',
    'oceania': 'oce',
    'turkey': 'tr',
    'russia': 'ru',
    'global': 'global'
}
