#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    sort(lost.begin(), lost.end());
    vector<bool> re(n + 1, false);
    vector<bool> lo(n + 1, false);
    vector<bool> can(n + 1, true);
    for (auto l : lost) {
        lo[l] = true;
    }
    for (auto r : reserve) {
        re[r] = true;
        if (lo[r]) {
            re[r] = false;
            lo[r] = false;
        }
    }
    for (int i = 1; i < n + 1; i++) {
        if (lo[i]) {
            if (i - 1 >= 1 && re[i - 1]) {
                re[i - 1] = false;
                continue;
            }
            if (i + 1 <= n && re[i + 1]) {
                re[i + 1] = false;
                continue;
            }
            can[i] = false;
        }
    }
    for (auto b : can) {
        if (b)
            answer += 1;
    }
    return answer - 1;
}