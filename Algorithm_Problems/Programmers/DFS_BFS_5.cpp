#include <string>
#include <vector>
#include <iostream>
#include <queue>
#include <cmath>

using namespace std;

int drawmap(vector<vector<int>> m) {
    for (int i = 0; i < m.size() / 2; i++) {
        for (int j = 0; j < m[0].size() / 2; j++) {
            cout << m[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}

int solution(vector<vector<int>> rectangle, int characterX, int characterY, int itemX, int itemY) {
    int answer = 0;
    vector<vector<int>> m(101, vector(101, 0));
    for (int i = 0; i < rectangle.size(); i++) {
        for (int j = rectangle[i][0] * 2; j < rectangle[i][2] * 2 + 1; j++) {
            for (int k = rectangle[i][1] * 2; k < rectangle[i][3] * 2 + 1; k++) {
                if (j == rectangle[i][0] * 2 || j == rectangle[i][2] * 2 || k == rectangle[i][1] * 2 || k == rectangle[i][3] * 2) {
                    m[j][k] = 1;
                }
                else {
                    continue;
                }
            }
        }
    }
    for (int i = 0; i < rectangle.size(); i++) {
        for (int j = rectangle[i][0] * 2; j < rectangle[i][2] * 2 + 1; j++) {
            for (int k = rectangle[i][1] * 2; k < rectangle[i][3] * 2 + 1; k++) {
                if (j == rectangle[i][0] * 2 || j == rectangle[i][2] * 2 || k == rectangle[i][1] * 2 || k == rectangle[i][3] * 2) {
                    continue;
                }
                else {
                    m[j][k] = 0;
                }
            }
        }
    }
    int sx = characterX * 2;
    int sy = characterY * 2;
    int ex = itemX * 2;
    int ey = itemY * 2;
    // cout << sx << sy << ex << ey << endl;
    // drawmap(m);
    int dx[4] = { 0, 0, -1, 1 };
    int dy[4] = { -1, 1, 0, 0 };
    queue<pair<int, int>> need_visited;
    need_visited.push(make_pair(sx, sy));
    while (!need_visited.empty()) {
        int tx = need_visited.front().first;
        int ty = need_visited.front().second;
        need_visited.pop();
        for (int i = 0; i < 4; i++) {
            int nx = tx + dx[i];
            int ny = ty + dy[i];
            if (0 <= nx && nx <= 100 && 0 <= ny && ny <= 100) {
                if (m[nx][ny] == 1) {
                    if (nx == ex && ny == ey) {
                        return (m[tx][ty] + 1) / 2;
                    }
                    need_visited.push(make_pair(nx, ny));
                    m[nx][ny] = m[tx][ty] + 1;
                }
            }
        }
    }
    return answer;
}