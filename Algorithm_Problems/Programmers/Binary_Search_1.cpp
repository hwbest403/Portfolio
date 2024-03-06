#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool comp(int a, int b) {
    return a > b;
}

long long solution(int n, vector<int> times) {
    sort(times.begin(), times.end(), comp);
    long long left = 1;
    long long right = (long)times.at(0) * n;
    long long answer = 0;
    long long mid;
    while (left <= right) {
        mid = (left + right) / 2;
        long long p = 0;
        // cout << left << " " << mid << " " << right << endl;
        for (auto num : times) {
            p += mid / num;
        }
        // cout << "p = " << p << endl;
        if (p >= n) {
            right = mid - 1;
            answer = mid;
        }
        else {
            left = mid + 1;
        }
    }

    return answer;
}