#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    vector<bool> visited(n, false);
    queue<int> need_visited;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            need_visited.push(i);
            while (!need_visited.empty()) {
                int tmp = need_visited.front();
                visited[tmp] = true;
                need_visited.pop();
                for (int j = 0; j < n; j++) {
                    if (tmp == j) {
                        continue;
                    }
                    else {
                        if (computers[tmp][j] == 1) {
                            if (!visited[j]) {
                                need_visited.push(j);
                            }
                        }
                    }
                }
            }
            answer += 1;
        }
    }
    return answer;
}