#include "summoner.h"
#include "leagueEnum.h"
#include "team.h"


Team::Team() : players(){}

void Team::addMember(Summoner* player, const std::string role){
    players[role] = player;
}

void Team::removeMember(const std::string role){
    players.erase(role);
}

int Team::getRoleRank(const std::string role) const{
    return players[role]->getRank();
}

int Team::getTeamRank() const{
    int ret = 0;
    for (auto& kv : players){
        ret += kv.second->getRank();
    }
    return ret / players.size();
}
