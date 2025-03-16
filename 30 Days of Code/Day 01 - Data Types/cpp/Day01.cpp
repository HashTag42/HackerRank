// HackerRank: 30 Days of Code - Day 1 : Data Types
// Problem : https ://www.hackerrank.com/challenges/30-data-types/problem?isFullScreen=true

#include <iostream>
#include <iomanip> // Required for setprecision()
#include <string>

using namespace std;

int main() {

    // Declare first integer, double, and String variables.
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";

    // INSERT YOUR CODE HERE

    // Declare second integer, double, and String variables.
	int i2;
	double d2;
    string s2;

    // Read and save an integer, double, and String to your variables.
	cin >> i2;
	cin.ignore();       // Ignore the newline character after the integer input
	
    cin >> d2;
    cin.ignore();
	
    getline(cin, s2);   // Using getline() to read a string with spaces

    // Print the sum of both integer variables on a new line.
	cout << i + i2 << endl;

    // Print the sum of the double variables on a new line.
	// The 'fixed' and 'setprecision' manipulators are used to format the output.
	cout << fixed << setprecision(1) << d + d2 << endl;

    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
	cout << s << s2 << endl;

	// END OF YOUR CODE

    return 0;
}