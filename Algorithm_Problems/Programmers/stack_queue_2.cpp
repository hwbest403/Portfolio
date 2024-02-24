#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int date = ceil(float(100 - progresses[0]) / speeds[0]);
    int flag = 0;
    for (int i = 0; i < progresses.size(); i++) {
        if (ceil(float(100 - progresses[i]) / speeds[i]) <= date) {
            flag += 1;
        }
        else {
            answer.push_back(flag);
            flag = 1;
            date = ceil(float(100 - progresses[i]) / speeds[i]);
        }
    }
    answer.push_back(flag);
    return answer;
}