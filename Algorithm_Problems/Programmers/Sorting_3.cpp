#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool comp(int a, int b) {
    return a > b;
}

int solution(vector<int> citations) {
    int answer = 0;
    sort(citations.begin(), citations.end(), comp);
    for (int i = 0; i < citations.size(); i++) {
        for (int j = citations[i]; j > citations[i + 1] - 1; j--) {
            if (j <= i + 1) {
                answer = max(answer, j);
            }
        }
    }
    return answer;
}