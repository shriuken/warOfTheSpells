__author__ = 'ryan'
# followed tutorial https://www.youtube.com/watch?v=0NycEiHOeX8

URL = {
    'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
    'champions': 'v{version}/champion',  # Retrieves all champions
    'champion_by_id_champion': 'v{version}/champion/{id}',  # Retrieve champion by id
    'current_game': 'observer-mode/rest/consumer/getSpectatorGameInfo/{platformId}/{summonerId}',  # Game info by id
    'featured_games': 'observer-mode/rest/featured',  # Get list of featured games
    'recent_games_by_summoner_id': 'v{version}/game/by-summoner/{summonerId}/recent',  # Get recent game by ids
    'leagues_by_summoner_id': 'v{version}/league/by-summoner/{summonerIds}',  # Get leagues mapped by summoner ids
    'league_entries_by_summoner_id': 'v{version}/league/by-summoner/{summonerIds}/entry',  # Get league entries by ids
    'leagues_by_team_id': 'v{version}/league/by-team/{teamIds}',  # Get leagues mapped by team ids
    'league_entries_by_team_id': 'v{version}/league/{teamIds}/entry',  # Get league entries by team ids
    'challenger': 'v{version}/league/challenger',  # Get challenger tier leagues
    'master': 'v{version}/league/master',  # Get master tier leagues
    'champion_list': 'static-data/{region}/v{version}/champion',  # Retrieves champion list
    'champion_by_id': 'static-data/{region}/v{version}/champion/{id}',  # Retrieve champion by id
    'item_list': 'static-data/{region}/v{version}/item',  # Retrieve item list
    'item_by_id': 'static-data/{region}/v{version}/item/{id}',  # Retrieves item by its unique id
    'language_strings': 'static-data/{region}/v{version}/language-strings',  # Retrieve language string data
    'supported_languages': 'static-data/{region}/v{version}/languages',  # Retrieve supported languages data
    'map': 'static-data/{region}/v{version}/map',  # Retrieve map data
    'mastery': 'static-data/{region}/v{version}/mastery',  # Retrieves mastery list
    'mastery_by_id': 'static-data/{region}/v{version}/mastery/{id}',  # Retrieves mastery item by id
    'realm': 'static-data/{region}/v{version}/realm',  # Retrieve realm data
    'rune': 'static-data/{region}/v{version}/rune',  # Retrieves rune list
    'rune_by_id': 'static-data/{region}/v{version}/rune/{id}',  # Retrieves rune by its unique id
    'summoner_spell': 'static-data/{region}/v{version}/summoner-spell',  # Retrieves summoner spell list
    'summoner_spell_by_id': 'static-data/{region}/v{version}/summoner-spell/{id}',  # Retrieves summoner spell by id
    'version': 'static-data/{region}/v{version}/versions',  # Retrieve version data
    'shard_list': 'shards',  # Get shard list.
    'shard_status': 'shards/{region}',  # Get shard status. Returns data from status.leagueoflegends.com
    'match_by_match_id': 'v{version}/match/{matchId}',  # Retrieve match by match id
    'match_list_by_summoner_id': 'v{version}/matchlist/by-summoner/{summonerId}',  # Retrieve match list by summoner id
    'ranked_stats_by_id': 'v{version}/stats/by-summoner/{summonerId}/ranked',  # Get ranked stats by summoner id
    'get_stats_summary_by_id': 'v{version}/stats/by-summoner/{summonerId}/summary',  # Get stat summaries by summoner id
    'summoner_by_name': 'v{version}/summoner/by-name/{names}',  # Gets summoner objects mapped by list of summoner names
    'summoner_by_id': 'v{version}/summoner/{summonerIds}',  # Gets summoner objects mapped by a list of summoner ids
    'summoner_masteries': 'v{version}/summoner/{summonerIds}/masteries',  # Get mastery pages mapped by summoner ids
    'summoner_name_by_id': 'v{version}/summoner/{summonerIds}/name',  # Get summoner names mapped by summoner ids
    'summoner_runes': 'v{version}/summoner/{summonerIds}/runes',  # Get rune pages mapped by summoner ids
    'team_by_summoner_id': 'v{version}/team/by-summoner/{summonerIds}',  # Get teams mapped by summoner ids
    'team_by_team_id': 'v{version}/team/{teamIds}'  # Get teams mapped by team ids
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
