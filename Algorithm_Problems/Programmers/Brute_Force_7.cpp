#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(string word) {
    int answer = 1;
    vector<char> vec = { 'A', 'E', 'I', 'O', 'U' };
    string str = "A";
    int flag = 0;
    while (true) {
        if (word == str)
            return answer;
        if (str.size() != 5) {
            flag += 1;
            str += vec[0];
            answer += 1;
        }
        else {
            bool stop_flag = false;
            while (true) {
                for (int i = 0; i < 5; i++) {
                    if (vec[i] == str.at(flag)) {
                        if (i < 4) {
                            str[flag] = vec[i + 1];
                            stop_flag = true;
                            answer += 1;
                            break;
                        }
                        else {
                            str.erase(flag, 1);
                            flag -= 1;
                        }
                    }
                }
                if (stop_flag)
                    break;
            }
        }
    }
    return answer;
}