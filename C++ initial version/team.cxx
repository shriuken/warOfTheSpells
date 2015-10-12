#include "summoner.h"
#include "leagueEnum.h"
#include "team.h"
#include "string"
#include "map"
#include "iostream"

Team::Team() : players(){}

void Team::addMember(Summoner* player, const LeagueEnums::Role role){
    players[role] = player;
}

Summoner* Team::removeMember(const LeagueEnums::Role role){
    Summoner* ret = players[role];
    players.erase(role);
    return ret;
}

int Team::getRoleRank(LeagueEnums::Role role){
    return players[role]->getRank();
}

int Team::getTeamRank() const{
    int ret = 0;
    for (auto &kv : players){
        ret += kv.second->getRank();
    }
    return ret / players.size();
}

void Team::print() const{
    //std::cout<< "Team Start:"<<std::endl;
    for (auto &kv:players){
        std::cout<<kv.second->getSummonerName()<< ", ";
    }
    std::cout<<"\nTeam Rank: "<<getTeamRank() << std::endl;
    //std::cout<<"Team End."<<std::endl;
}
