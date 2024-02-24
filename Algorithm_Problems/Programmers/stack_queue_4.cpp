#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <deque>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 1;
    priority_queue<int> pq;
    queue<int> v;
    for (int i = 0; i < priorities.size(); i++) {
        pq.push(priorities[i]);
        v.push(i);
    }
    while (true) {
        if (priorities.front() < pq.top()) {
            priorities.push_back(priorities.front());
            priorities.erase(priorities.begin());
            v.push(v.front());
            v.pop();
        }
        else {
            if (v.front() == location) {
                return answer;
            }
            else {
                v.pop();
                priorities.erase(priorities.begin());
                pq.pop();
                answer += 1;
            }
        }
    }
}