#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> wires) {
    int answer = 100;
    map<int, vector<int>> m;
    for (int i = 0; i < wires.size(); i++) {
        m[wires[i][0]].push_back(wires[i][1]);
        m[wires[i][1]].push_back(wires[i][0]);
    }
    for (int i = 0; i < wires.size(); i++) {
        vector<int> tmp = { wires[i][0], wires[i][1] };
        queue<int> need_visited;
        vector<bool> visited(n + 1, false);
        need_visited.push(1);
        int cnt = 1;
        // cout << tmp[0] << tmp[1] << endl;
        while (!need_visited.empty()) {
            int tnode = need_visited.front();
            need_visited.pop();
            visited[tnode] = true;
            // cout << "tnode: " << tnode << endl;
            for (int j = 0; j < m[tnode].size(); j++) {
                if (!visited[m[tnode][j]]) {
                    if (tnode == tmp[0] && m[tnode][j] == tmp[1])
                        continue;
                    if (tnode == tmp[1] && m[tnode][j] == tmp[0])
                        continue;
                    need_visited.push(m[tnode][j]);
                    cnt += 1;
                }
            }
        }
        answer = min(answer, abs((n - cnt) - cnt));
    }
    return answer;
}