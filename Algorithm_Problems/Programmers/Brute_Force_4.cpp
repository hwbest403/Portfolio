#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    for (int i = 1; i < (brown + 4) / 2; i++) {
        if (i * ((brown + 4) / 2 - i) == brown + yellow) {
            answer.push_back((brown + 4) / 2 - i);
            answer.push_back(i);
            return answer;
        }
    }
    return { 0 };
}