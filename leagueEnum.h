#ifndef _LEAGUEENUMS_
#define _LEAGUEENUMS_

#include "string"
#include "map"

namespace LeagueEnums{
    enum League{
        unranked = 25,//when doing rank math this should be 35*1 versus 7*5
        bronze = 6,
        silver = 5,
        gold = 4,
        platinum = 3,
        diamond = 2,
        masters = 1,
        challenger = 0
    };
    
    enum Role{
        top = 0,
        jungle = 1,
        mid = 2,
        marksman = 3,
        support = 4,
        noroll = 5
    };
}

#endif
