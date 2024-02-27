#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool comp(int a, int b) {
    return to_string(a) + to_string(b) > to_string(b) + to_string(a);
}

string solution(vector<int> numbers) {
    string answer = "";
    if (count(numbers.begin(), numbers.end(), 0) == numbers.size()) {
        return "0";
    }
    sort(numbers.begin(), numbers.end(), comp);
    for (auto num : numbers) {
        answer += to_string(num);
    }
    return answer;
}