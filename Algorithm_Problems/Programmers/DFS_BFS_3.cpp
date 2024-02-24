#include<vector>
#include<iostream>
#include<queue>

using namespace std;

int solution(vector<vector<int>> maps)
{
    int answer = 0;
    int ix = 0;
    int iy = 0;
    int ex = maps.size() - 1;
    int ey = maps[0].size() - 1;
    int dx[4] = { 0, 0, 1, -1 };
    int dy[4] = { -1, 1, 0, 0 };
    queue<pair<int, int>> need_visited;
    vector<vector<int>> visited(maps.size(), vector<int>(maps[0].size(), -1));
    need_visited.push(make_pair(ix, iy));
    while (!need_visited.empty()) {
        int tx = need_visited.front().first;
        int ty = need_visited.front().second;
        need_visited.pop();
        if (ix == 0 && iy == 0) {
            visited[ix][iy] = 1;
        }
        for (int i = 0; i < 4; i++) {
            int nx = tx + dx[i];
            int ny = ty + dy[i];
            if (ix <= nx && nx <= ex && iy <= ny && ny <= ey && visited[nx][ny] == -1 && maps[nx][ny] == 1) {
                if (nx == ex && ny == ey) {
                    return visited[tx][ty] + 1;
                }
                visited[nx][ny] = visited[tx][ty] + 1;
                need_visited.push(make_pair(nx, ny));
            }
        }
    }
    return -1;
}