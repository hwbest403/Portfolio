#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int answer = 0;
    int max_h = 0;
    vector<int> vec2;
    for (int i = 0; i < sizes.size(); i++) {
        max_h = max(max_h, max(sizes[i][0], sizes[i][1]));
        vec2.push_back(min(sizes[i][0], sizes[i][1]));
    }
    sort(vec2.begin(), vec2.end());
    answer = max_h * vec2[vec2.size() - 1];
    return answer;
}