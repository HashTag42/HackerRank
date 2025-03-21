// HackerRank: 30 Days of Code: Day 21: Generics
// Problem: https://www.hackerrank.com/challenges/30-generics/problem?isFullScreen=true

#include <iostream>
#include <vector>

using namespace std;

template<typename T>
void printArray(const vector<T> v)
{
    for (T element : v)
        cout << element << endl;

    return;
}

int main()
{
    int count;

    cin >> count;
    vector<int> int_vector(count);
    for (int i = 0; i < count; i++)
        cin >> int_vector[i];

    cin >> count;
    vector<string> string_vector(count);
    for (int i = 0; i < count; i++)
        cin >> string_vector[i];

    printArray(int_vector);
    printArray(string_vector);

    return 0;
}
