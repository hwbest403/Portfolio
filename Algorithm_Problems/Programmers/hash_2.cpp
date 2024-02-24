#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    multiset<string> st;
    for (auto str : participant) {
        st.insert(str);
    }
    for (auto str : completion) {
        multiset<string>::iterator it = st.find(str);
        st.erase(it);
    }
    return *st.begin();
}