#include "tsvReader.h"
#include "vector"
#include "string"
#include "iostream"
#include "fstream"
#include "sstream"

tsvReader::tsvReader() : rows(){}

//credit: http://stackoverflow.com/questions/1075712/reading-delimited-files-in-c
std::vector<std::vector<std::string>> tsvReader::readTsv(std::string filename){
    typedef std::vector<std::vector<std::string>> Rows;
    std::ifstream input(filename);
    Rows file;
    char const row_delim = '\n';
    char const field_delim = '\t';
    for (std::string row; std::getline(input, row, row_delim); ) {
        file.push_back(Rows::value_type());
        std::istringstream ss(row);
        for (std::string field; std::getline(ss, field, field_delim); ) {
            file.back().push_back(field);
        }
    }
    return file;
}
