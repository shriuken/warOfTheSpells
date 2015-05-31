#ifndef _TEAM_
#define _TEAM_

#include "summoner.h"
#include "leagueEnum.h"

class Team{
public:
    Team();
    
private:
    std::map<std::string, Summoner*> players;
    

};



#endif
