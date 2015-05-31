#include "summoner.h"
#include "leagueEnum.h"

Summoner::Summoner():
sname("Default"), 
pname("Default"), 
league(), 
division(1), 
primaryRole(0),
secndryRole(0)
{}

void Summoner::setSummonerName(const std::string& name){
    sname = name;
}

void Summoner::setPlayerName(const std::string& name){
    pname = name;
}

void Summoner::setLeague(const LeagueEnums::League newLeague){
    league = newLeague;
}

void Summoner::setDivision(const int div){
    division = div;
}

void Summoner::setPrimaryRole(const LeagueEnums::Role prim){
    primaryRole = prim;
}

void Summoner::setSecndryRole(const LeagueEnums::Role scnd){
    secndryRole = scnd;
}

std::string Summoner::getSummonerName() const{
    return sname;
}

std::string Summoner::getPlayerName() const{
    return pname;
}

LeagueEnums::League Summoner::getLeague() const{
    return league;
}

int Summoner::getDivision() const{
    return division;
}

int Summoner::getRank() const{
    return division*league;
}

LeagueEnums::Role getPrimaryRole() const{
    return primaryRole;
}

LeagueEnums::Role getSecndryRole() const{
    return secndryRole;
}
