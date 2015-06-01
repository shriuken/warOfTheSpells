#include "iostream"
#include "string"
#include "vector"
#include "tsvReader.h"
#include "stack"
#include "summoner.h"

void createMappings(std::map<std::string, LeagueEnums::League> lmap, 
                   std::map<std::string, LeagueEnums::Role> rmap, 
                   std::map<std::string, int> dmap){
    lmap["Unranked"] = LeagueEnums::unranked;
    lmap["Bronze"] = LeagueEnums::bronze;
    lmap["Silver"] = LeagueEnums::silver;
    lmap["Gold"] = LeagueEnums::gold;
    lmap["Platinum"] = LeagueEnums::platinum;
    lmap["Diamond"] = LeagueEnums::diamond;
    lmap["Masters"] = LeagueEnums::masters;
    lmap["Challenger"] = LeagueEnums::challenger;
    
    rmap["Marksman"] = LeagueEnums::marksman;
    rmap["Support"] = LeagueEnums::support;
    rmap["Mid Lane"] = LeagueEnums::mid;
    rmap["Jungle"] = LeagueEnums::jungle;
    rmap["Top Lane"] = LeagueEnums::top;
    
    dmap["I"] = 1;
    dmap["II"] = 2;
    dmap["III"] = 3;
    dmap["IV"] = 4;
    dmap["V"] = 5;
    
}

//credit: http://www.cplusplus.com/articles/2wA0RXSz/
const std::vector<std::string> explode(const std::string& s, const char&c = ' '){
    std::string buff{""};
    std::vector<std::string> v;
    
    for (auto n : s){
        if (n != c){
            buff+=n;
        }
        else if (n == c && buff != ""){
            v.push_back(buff);
            buff = "";
        }        
    }
    if (buff != ""){
        v.push_back(buff);
    }
    return v;
}

int main(int argc, char* argv []){
    std::map<std::string, LeagueEnums::League> leagueMap;
    std::map<std::string, LeagueEnums::Role> roleMap;
    std::map<std::string, int> divMap;
    
    //horrible fix, and I'm a terrible programmer for implementing this.
    createMappings(leagueMap, roleMap, divMap);
    
    tsvReader filereader;
    std::vector<std::vector<std::string>> file;
    std::vector<Summoner*> summoners;
    if (argc > 1){
        file = filereader.readTsv(argv[1]);
        for (size_t x = 0; x < file.size(); x++){
            Summoner* summoner = new Summoner();
            summoner->setPlayerName(file[x][1]);//1 is name
            summoner->setSummonerName(file[x][3]);//3 is summoner name
            summoner->setPrimaryRole(roleMap[file[x][4]]);
            if (file[x][5] != ""){
                summoner->setSecndryRole(roleMap[file[x][5]]);
            }
            summoner->setLeague(leagueMap[explode(file[x][6])[0]]);
            if (summoner->getLeague() != LeagueEnums::challenger and
                summoner->getLeague() != LeagueEnums::masters and
                summoner->getLeague() != LeagueEnums::unranked)
            {
                summoner->setDivision(divMap[explode(file[x][6])[1]]);
            }
        }
    }
    
    
    //TODO:  Add logic for sorting and creating teams. 
    //       Add garbage collection for program.   
    return 1;
}
