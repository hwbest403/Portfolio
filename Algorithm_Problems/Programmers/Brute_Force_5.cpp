#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(int k, vector<vector<int>> dungeons) {
    int answer = -1;
    vector<int> vec;
    for (int i = 0; i < dungeons.size(); i++) {
        vec.push_back(i);
    }
    do {
        int tmp = 0;
        int tmp_k = k;
        for (int i = 0; i < vec.size(); i++) {
            if (tmp_k >= dungeons[vec[i]][0]) {
                tmp_k -= dungeons[vec[i]][1];
                tmp += 1;
            }
            else {
                break;
            }
        }
        answer = max(answer, tmp);
    } while (next_permutation(vec.begin(), vec.end()));
    return answer;
}