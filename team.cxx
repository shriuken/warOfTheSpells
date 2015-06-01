#include "summoner.h"
#include "leagueEnum.h"
#include "team.h"
#include "string"
#include "map"

Team::Team() : players(){}

void Team::addMember(Summoner* player, const LeagueEnums::Role role){
    players[role] = player;
}

void Team::removeMember(const LeagueEnums::Role role){
    players.erase(role);
}

int Team::getRoleRank(LeagueEnums::Role role){
    return players[role]->getRank();
}

int Team::getTeamRank() const{
    int ret = 0;
    for (auto& kv : players){
        ret += kv.second->getRank();
    }
    return ret / players.size();
}
