#include <string>
#include <iostream>
#include <vector>

using namespace std;

bool solution(string s)
{
    vector<char> v;
    for (int i = 0; i < s.length(); i++) {
        if (s.at(i) == '(') {
            v.push_back(s.at(i));
        }
        else {
            if (v.size() == 0) {
                return false;
            }
            else {
                v.pop_back();
            }
        }
    }
    if (v.size() != 0) {
        return false;
    }
    return true;
}