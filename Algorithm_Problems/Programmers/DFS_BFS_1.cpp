#include <string>
#include <vector>
#include <iostream>

using namespace std;
int answer = 0;

int bf(vector<int> numbers, int a, int target, int size, int flag) {
    if (flag == size) {
        if (a == target) {
            answer += 1;
            return 0;
        }
        return 0;
    }
    bf(numbers, a + numbers.at(flag), target, size, flag + 1);
    bf(numbers, a - numbers.at(flag), target, size, flag + 1);
    return 0;
}

int solution(vector<int> numbers, int target) {
    bf(numbers, 0, target, numbers.size(), 0);
    return answer;
}