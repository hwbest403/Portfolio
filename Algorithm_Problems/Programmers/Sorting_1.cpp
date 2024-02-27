#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for (int i = 0; i < commands.size(); i++) {
        vector<int> t_vec;
        for (int j = commands[i][0] - 1; j < commands[i][1]; j++) {
            t_vec.push_back(array[j]);
        }
        sort(t_vec.begin(), t_vec.end());
        answer.push_back(t_vec[commands[i][2] - 1]);
    }
    return answer;
}