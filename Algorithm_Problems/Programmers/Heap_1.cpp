#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

struct comp {
    bool operator() (int a, int b) {
        return a > b;
    }
};

int solution(vector<int> scoville, int K) {
    int answer = 0;
    priority_queue<int, vector<int>, comp> q;
    for (auto num : scoville) {
        q.push(num);
    }
    while (true) {
        if (q.top() >= K) {
            break;
        }
        else if (q.size() == 1) {
            return -1;
        }
        int tmp = q.top();
        q.pop();
        q.push(tmp + q.top() * 2);
        q.pop();
        answer += 1;
    }
    return answer;
}