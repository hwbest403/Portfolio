#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>
#include <cmath>

using namespace std;

struct p {
    int x, y;
};

typedef struct p p;

struct comp {
    bool operator() (p& a, p& b) {
        return a.y > b.y;
    }
};

int solution(vector<vector<int>> jobs) {
    long long int answer = 0;
    sort(jobs.begin(), jobs.end());
    priority_queue<p, vector<p>, comp> pq;
    int t = -1;
    int idx = 0;
    int flag = 0;
    while (flag < jobs.size()) {
        if (idx != jobs.size() && t < jobs[idx][0] && pq.empty()) {
            t = jobs[idx][0];
        }
        for (int i = idx; i < jobs.size(); i++) {
            if (jobs[i][0] <= t) {
                p tmp;
                tmp.x = jobs[i][0];
                tmp.y = jobs[i][1];
                pq.push(tmp);
                if (i == jobs.size() - 1) {
                    idx = jobs.size();
                    break;
                }
            }
            else {
                idx = i;
                break;
            }
        }
        t += pq.top().y;
        answer += t - pq.top().x;
        flag += 1;
        pq.pop();
    }
    return floor(answer / jobs.size());
}