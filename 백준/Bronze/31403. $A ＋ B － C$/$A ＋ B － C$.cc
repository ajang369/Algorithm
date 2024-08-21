#include <iostream>
#include <string>
using namespace std;
int main()
{
	int A = 0;
	int B = 0;
	int C = 0;
	cin >> A;
	cin >> B;
	cin >> C;

	string str_a = to_string(A);
	string str_b = to_string(B);
	int result1 = A + B - C;
	int result2 = stoi(str_a + str_b) - C;

	cout << result1 << endl;
	cout << result2;
	return 0;
}