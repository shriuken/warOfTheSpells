#ifndef _TEAM_
#define _TEAM_

#include "summoner.h"
#include "leagueEnum.h"

#include "map"

class Team{
public:
    Team();
    
    void addMember(Summoner* player, const LeagueEnums::Role role);
    Summoner* removeMember(const LeagueEnums::Role role); 
    
    int getRoleRank(LeagueEnums::Role role);
    int getTeamRank() const;
    
    void print() const;
    
private:
    std::map<LeagueEnums::Role, Summoner*> players;
};



#endif
