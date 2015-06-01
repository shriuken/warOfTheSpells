#ifndef _TEAM_
#define _TEAM_

#include "summoner.h"
#include "leagueEnum.h"

class Team{
public:
    Team();
    
    void addMember(Summoner* player, const std::string role);
    void removeMember(const std::string role); 
    
    int getRoleRank(const std::string role) const;
    int getTeamRank() const;
    
private:
    std::map<std::string, Summoner*> players;
};



#endif
