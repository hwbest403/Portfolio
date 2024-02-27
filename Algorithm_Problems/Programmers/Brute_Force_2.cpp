#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> n1 = { 1, 2, 3, 4, 5 };
    vector<int> n2 = { 2, 1, 2, 3, 2, 4, 2, 5 };
    vector<int> n3 = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, };
    int nc1 = 0, nc2 = 0, nc3 = 0;
    for (int i = 0; i < answers.size(); i++) {
        if (answers[i] == n1[i % 5]) {
            nc1 += 1;
        }
        if (answers[i] == n2[i % 8]) {
            nc2 += 1;
        }
        if (answers[i] == n3[i % 10]) {
            nc3 += 1;
        }
    }
    int max_c = max(nc1, max(nc2, nc3));
    if (max_c == nc1) {
        answer.push_back(1);
    }
    if (max_c == nc2) {
        answer.push_back(2);
    }
    if (max_c == nc3) {
        answer.push_back(3);
    }
    return answer;
}