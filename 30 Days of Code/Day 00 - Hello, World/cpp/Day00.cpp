// HackerRank.com: 30 Days of Code - Day 0 : Hello, World.
// Problem : https ://www.hackerrank.com/challenges/30-hello-world/problem?isFullScreen=true

#include <iostream>
#include <string>

using namespace std;

int main()
{
	string message;

	getline(cin, message);	// Using getline() to read a string with spaces
    
	cout << "Hello, World.\n";

	cout << message << endl;
}
