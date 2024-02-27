#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int prime(int a) {
    if (a == 0 || a == 1) {
        return 0;
    }
    if (a == 2) {
        return 2;
    }
    if (a == 3) {
        return 3;
    }
    for (int i = 2; i < a / 2 + 1; i++) {
        if (a % i != 0) {
            continue;
        }
        return 0;
    }
    return a;
}

int solution(string numbers) {
    int answer = 0;
    map<int, bool> m;
    sort(numbers.begin(), numbers.end());
    do {
        for (int i = 0; i < numbers.size(); i++) {
            for (int j = 1; j < numbers.size() + 1 - i; j++) {
                int tmp = stoi(numbers.substr(i, j));
                if (m[tmp] == false) {
                    m[tmp] = true;
                    if (prime(tmp) != 0) {
                        answer += 1;
                    }
                }
            }
        }
    } while (next_permutation(numbers.begin(), numbers.end()));
    return answer;
}