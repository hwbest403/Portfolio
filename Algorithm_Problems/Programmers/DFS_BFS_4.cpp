#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <queue>

using namespace std;

int solution(string begin, string target, vector<string> words) {
    int answer = 0;
    map<int, vector<int>> m;
    words.push_back(begin);
    int s = words.size() - 1;
    int t = -1;
    for (int i = 0; i < words.size() - 1; i++) {
        if (words[i] == target) {
            t = i;
        }
        for (int j = i + 1; j < words.size(); j++) {
            int flag = 0;
            for (int k = 0; k < words[0].length(); k++) {
                if (words[i][k] != words[j][k]) {
                    flag += 1;
                }
            }
            if (flag == 1) {
                m[i].push_back(j);
                m[j].push_back(i);
            }
        }
    }
    if (words[words.size() - 1] == target) {
        t = words.size() - 1;
    }
    if (t == -1) {
        return 0;
    }
    vector<int> visited(words.size(), -1);
    queue<int> need_visited;
    need_visited.push(s);
    visited[s] = 0;
    while (!need_visited.empty()) {
        int tmp = need_visited.front();
        need_visited.pop();
        for (int i = 0; i < m[tmp].size(); i++) {
            if (visited[m[tmp][i]] == -1) {
                if (m[tmp][i] == t) {
                    return visited[tmp] + 1;
                }
                need_visited.push(m[tmp][i]);
                visited[m[tmp][i]] = visited[tmp] + 1;
            }
        }
    }
    return 0;
}