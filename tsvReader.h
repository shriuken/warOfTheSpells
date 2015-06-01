#ifndef _TSVREADER_
#define _TSVREADER_

#include "string"
#include "vector"

class TSVReader{
public:
    TSVReader();
    
    readTSV(std::string filename);
    
private:
    std::vector<std::vector<std::string>> rows;

}


#endif
