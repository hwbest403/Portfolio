#include <iostream>
#include <vector>
#include <map>

using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    map<int, int> m;
    int max_size = nums.size() / 2;
    for (auto i : nums) {
        m[i] += 1;
    }
    if (m.size() < max_size) {
        answer = m.size();
    }
    else {
        answer = max_size;
    }
    return answer;
}