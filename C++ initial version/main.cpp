#include "iostream"
#include "string"
#include "vector"
#include "tsvReader.h"
#include "stack"
#include "summoner.h"
#include "set"
#include "team.h"

//g++ -std=c++11 summoner.cxx team.cxx tsvReader.cxx main.cpp


void createMappings(std::map<std::string, LeagueEnums::League> &lmap, 
                   std::map<std::string, LeagueEnums::Role> &rmap, 
                   std::map<std::string, int> &dmap){
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
    
    //std::cout<<"Marksman: "<< rmap["Marksman"]<<std::endl;
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
    
    std::vector<Summoner*> markMain;
    std::vector<Summoner*> suppMain;
    std::vector<Summoner*> midlMain;
    std::vector<Summoner*> jungMain;
    std::vector<Summoner*> toplMain;
    
    std::vector<Summoner*> markOff;
    std::vector<Summoner*> suppOff;
    std::vector<Summoner*> midlOff;
    std::vector<Summoner*> jungOff;
    std::vector<Summoner*> toplOff;
    
    //horrible fix, and I'm a terrible programmer for implementing this.
    createMappings(leagueMap, roleMap, divMap);
    
    tsvReader filereader;
    std::vector<std::vector<std::string>> file;
    std::vector<Summoner*> summoners;
    if (argc > 1){
        file = filereader.readTsv(argv[1]);
        std::set<std::string> ignSet;
        for (size_t x = 1; x < file.size(); x++){
            if (ignSet.count(file[x][3]) == 0){//add unique summoner names to list
                Summoner* summoner = new Summoner();
                summoners.push_back(summoner);
                summoner->setPlayerName(file[x][1]);//1 is name
                summoner->setSummonerName(file[x][3]);//3 is summoner name
                //std::cout<<"Adding summoner: "<<summoner->getSummonerName()<<std::endl;
                summoner->setPrimaryRole(roleMap[file[x][4]]);
                //std::cout<<"role string: " << file[x][4] << std::endl;
                //std::cout<<"role map: "<<roleMap[file[x][4]]<<std::endl;
                
                //ugly logic tree inc
                if (file[x][4] == "Marksman"){//might be unnecessary...
                    markMain.push_back(summoner);
                }
                else if (file[x][4] == "Support"){
                    suppMain.push_back(summoner);
                }
                else if (file[x][4] == "Jungle"){
                    jungMain.push_back(summoner);
                }
                else if (file[x][4] == "Mid Lane"){
                    midlMain.push_back(summoner);
                }
                else if (file[x][4] == "Top Lane"){
                    toplMain.push_back(summoner);
                }
                
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
    }
    //begin team generation
    int numTeams = summoners.size() / 5;
    std::vector<Team*> teams;
    for (int x = 0; x < numTeams; x++){
        Team* team = new Team;
        teams.push_back(team);
    }
    //add ADCs primary
    std::set<int> indexUsed;
    int lastTeamAdded = 0;
    for (int x = 0; x < numTeams; x++){
        int index = 0;
        int numUsed = indexUsed.size();
        while (index < summoners.size()){
            //std::cout<<"Summoner: " << summoners[index]->getSummonerName();
            //std::cout<<", role: "<<summoners[index]->getPrimaryRole()<<std::endl;
            if (summoners[index]->getPrimaryRole() == LeagueEnums::marksman){
                //std::cout<<"Match found!"<<std::endl;
                if (indexUsed.count(index) == 0){
                    //std::cout<<"Add add member if statement." << std::endl;
                    teams[x]->addMember(summoners[index], LeagueEnums::marksman);
                    indexUsed.insert(index);
                    index++;  
                    lastTeamAdded = x;
                    break;
                }
            }
            index++;
        }
    }
    
    //add ADCs secondary
    for (int x = lastTeamAdded; x < numTeams; x++){
        int index = 0;
        int numUsed = indexUsed.size();
        while (index < summoners.size()){
            //std::cout<<"Summoner: " << summoners[index]->getSummonerName();
            //std::cout<<", role: "<<summoners[index]->getPrimaryRole()<<std::endl;
            if (summoners[index]->getSecndryRole() == LeagueEnums::marksman){
                //std::cout<<"Match found!"<<std::endl;
                if (indexUsed.count(index) == 0){
                    //std::cout<<"Add add member if statement." << std::endl;
                    teams[x]->addMember(summoners[index], LeagueEnums::marksman);
                    indexUsed.insert(index);
                    index++;  
                    lastTeamAdded = x;
                    break;
                }
            }
            index++;
        }      
    }
    lastTeamAdded = 0;
    
    //add supports
    //std::cout<<"Support Numbers: " << suppMain.size()<<std::endl;
    for (int x = 0; x < numTeams; x++){
        int index = 0;
        int numUsed = indexUsed.size();
        while (index < summoners.size()){
            //std::cout<<"Summoner: " << summoners[index]->getSummonerName();
            //std::cout<<", role: "<<summoners[index]->getPrimaryRole()<<std::endl;
            if (summoners[index]->getPrimaryRole() == LeagueEnums::support){
                //std::cout<<"Match found!"<<std::endl;
                if (indexUsed.count(index) == 0){
                    //std::cout<<"Add add member if statement." << std::endl;
                    teams[x]->addMember(summoners[index], LeagueEnums::support);
                    indexUsed.insert(index);
                    index++;
                    lastTeamAdded = x;
                    break;
                }
            }
            index++;
        }
    }
    //secondary supports
    //std::cout<<"lastTeamAdded: " << lastTeamAdded << std::endl;
    for (int x = lastTeamAdded; x < numTeams; x++){
        int index = 0;
        int numUsed = indexUsed.size();
        while (index < summoners.size()){
            //std::cout<<"Summoner: " << summoners[index]->getSummonerName();
            //std::cout<<", role: "<<summoners[index]->getPrimaryRole()<<std::endl;
            if (summoners[index]->getSecndryRole() == LeagueEnums::support){
                //std::cout<<"Match found!"<<std::endl;
                if (indexUsed.count(index) == 0){
                    //std::cout<<"Add add member if statement." << std::endl;
                    teams[x]->addMember(summoners[index], LeagueEnums::support);
                    indexUsed.insert(index);
                    index++;  
                    lastTeamAdded = x;
                    break;
                }
            }
            index++;
        }      
    }
    lastTeamAdded = 0;
    
    //add mids
    //std::cout<<"Support Numbers: " << suppMain.size()<<std::endl;
    for (int x = 0; x < numTeams; x++){
        int index = 0;
        int numUsed = indexUsed.size();
        while (index < summoners.size()){
            //std::cout<<"Summoner: " << summoners[index]->getSummonerName();
            //std::cout<<", role: "<<summoners[index]->getPrimaryRole()<<std::endl;
            if (summoners[index]->getPrimaryRole() == LeagueEnums::mid){
                //std::cout<<"Match found!"<<std::endl;
                if (indexUsed.count(index) == 0){
                    //std::cout<<"Add add member if statement." << std::endl;
                    teams[x]->addMember(summoners[index], LeagueEnums::mid);
                    indexUsed.insert(index);
                    index++;
                    lastTeamAdded = x;
                    break;
                }
            }
            index++;
        }
    }
    //secondary mids
    for (int x = lastTeamAdded; x < numTeams; x++){
        int index = 0;
        int numUsed = indexUsed.size();
        while (index < summoners.size()){
            //std::cout<<"Summoner: " << summoners[index]->getSummonerName();
            //std::cout<<", role: "<<summoners[index]->getPrimaryRole()<<std::endl;
            if (summoners[index]->getSecndryRole() == LeagueEnums::mid){
                //std::cout<<"Match found!"<<std::endl;
                if (indexUsed.count(index) == 0){
                    //std::cout<<"Add add member if statement." << std::endl;
                    teams[x]->addMember(summoners[index], LeagueEnums::mid);
                    indexUsed.insert(index);
                    index++;  
                    lastTeamAdded = x;
                    break;
                }
            }
            index++;
        }      
    }
    lastTeamAdded = 0;
    
    for (int x = 0; x < numTeams; x++){
        int index = 0;
        int numUsed = indexUsed.size();
        while (index < summoners.size()){
            //std::cout<<"Summoner: " << summoners[index]->getSummonerName();
            //std::cout<<", role: "<<summoners[index]->getPrimaryRole()<<std::endl;
            if (summoners[index]->getPrimaryRole() == LeagueEnums::jungle){
                //std::cout<<"Match found!"<<std::endl;
                if (indexUsed.count(index) == 0){
                    //std::cout<<"Add add member if statement." << std::endl;
                    teams[x]->addMember(summoners[index], LeagueEnums::jungle);
                    indexUsed.insert(index);
                    index++;
                    lastTeamAdded = x;
                    break;
                }
            }
            index++;
        }
    }
    //secondary jg
    for (int x = lastTeamAdded; x < numTeams; x++){
        int index = 0;
        int numUsed = indexUsed.size();
        while (index < summoners.size()){
            //std::cout<<"Summoner: " << summoners[index]->getSummonerName();
            //std::cout<<", role: "<<summoners[index]->getPrimaryRole()<<std::endl;
            if (summoners[index]->getSecndryRole() == LeagueEnums::jungle){
                //std::cout<<"Match found!"<<std::endl;
                if (indexUsed.count(index) == 0){
                    //std::cout<<"Add add member if statement." << std::endl;
                    teams[x]->addMember(summoners[index], LeagueEnums::jungle);
                    indexUsed.insert(index);
                    index++;  
                    lastTeamAdded = x;
                    break;
                }
            }
            index++;
        }      
    }
    lastTeamAdded = 0;
    
    for (int x = 0; x < numTeams; x++){
        int index = 0;
        int numUsed = indexUsed.size();
        while (index < summoners.size()){
            //std::cout<<"Summoner: " << summoners[index]->getSummonerName();
            //std::cout<<", role: "<<summoners[index]->getPrimaryRole()<<std::endl;
            if (summoners[index]->getPrimaryRole() == LeagueEnums::top){
                //std::cout<<"Match found!"<<std::endl;
                if (indexUsed.count(index) == 0){
                    //std::cout<<"Add add member if statement." << std::endl;
                    teams[x]->addMember(summoners[index], LeagueEnums::top);
                    indexUsed.insert(index);
                    index++;
                    lastTeamAdded = x;
                    break;
                }
            }
            index++;
        }
    }
    //secondary top
    for (int x = lastTeamAdded; x < numTeams; x++){
        int index = 0;
        int numUsed = indexUsed.size();
        while (index < summoners.size()){
            //std::cout<<"Summoner: " << summoners[index]->getSummonerName();
            //std::cout<<", role: "<<summoners[index]->getPrimaryRole()<<std::endl;
            if (summoners[index]->getSecndryRole() == LeagueEnums::top){
                //std::cout<<"Match found!"<<std::endl;
                if (indexUsed.count(index) == 0){
                    //std::cout<<"Add add member if statement." << std::endl;
                    teams[x]->addMember(summoners[index], LeagueEnums::top);
                    indexUsed.insert(index);
                    index++; 
                    lastTeamAdded = x;
                    break;
                }
            }
            index++;
        }      
    }
    lastTeamAdded = 0;
    
    
    //std::cout<<"index: "<<index<<std::endl;
    //print
    for (int x = 0; x < numTeams; x++){
        teams[x]->print();
    }
    
    //std::cout<<"team4 mid rank:"<<teams[4]->getRoleRank(LeagueEnums::mid)<<std::endl;
    
    /*std::cout<<"Unranked: " << LeagueEnums::unranked<<std::endl;
    std::cout<<"Silver: " << LeagueEnums::silver<<std::endl;
    std::cout<<"Platinum: " << LeagueEnums::platinum<<std::endl;
    */
    //TODO:  Add logic for sorting and creating teams. 
    //       Add garbage collection for program.   
    return 1;
}
