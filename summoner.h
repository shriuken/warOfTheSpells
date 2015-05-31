#ifndef _SUMMONER_
#define _SUMMONER_


#include "leagueEnum.h" 

class Summoner{
public:
    Summoner();
    //other constructors if necessary before this.
    
    //set private data members
    void setSummonerName(const std::string& name);
    void setPlayerName(const std::string& name);
    
    void setLeague(const LeagueEnums::League newLeague);
    void setDivision(const int div);
    
    void setPrimaryRole(const LeagueEnums::Role prim);
    void setSecndryRole(const LeagueEnums::Role scnd);
    
    //get private data members
    std::string getSummonerName() const;
    std::string getPlayerName() const;
    
    LeagueEnums::League getLeague() const;
    int getDivision() const;
    int getRank() const;
    
    LeagueEnums::Role getPrimaryRole() const;
    LeagueEnums::Role getSecndryRole() const;
    


private:
    std::string sname;
    std::string pname;
    
    LeagueEnums::League league;
    int division;
    
    LeagueEnums::Role primaryRole;
    LeagueEnums::Role secndryRole;
    
    
    
    


};




#endif
