#ifndef _TSVREADER_
#define _TSVREADER_

#include "string"
#include "vector"

class tsvReader{
public:
    tsvReader();
    
    std::vector<std::vector<std::string>> readTsv(std::string filename);
    
private:
    std::vector<std::vector<std::string>> rows;

};


#endif
