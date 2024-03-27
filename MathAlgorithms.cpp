#include <iostream>
using namespace std;

int main () {

    // list of options:

    cout << "1) fibonnaci series\n2) show prime number\n3) LCM\n4) calculate factorial\n\
5) ceck-odd-even\n6) check perfect number\n7) pythagorean numbers\n8) discount calculation\n\
9) GCD" << endl;

    // programs progress

    // 1:

/*    int n, t1 = 0, t2 = 1, nextTerm = 0;

    cout << "Enter the number of terms: ";
    cin >> n;

    cout << "Fibonacci Series: ";

    for (int i = 1; i <= n; ++i) {

        if(i == 1) {
            cout << t1 << " ";
            continue;
        }
        if(i == 2) {
            cout << t2 << " ";
            continue;
        }
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;

        cout << nextTerm << " ";
    }
*/


    // 2:

 /*   int n;
    bool isPrime = true;

    cout << "Enter the number: ";
    cin >> n;

    for (int i = 2; i < n/2; i++) {
        if (n % i == 0) {
            isPrime = false;
            break;
        }
    }

    if (isPrime && n > 1) {
        cout << n << " is a prime number." << endl;
    }
    else {
        cout << n << " is not a prime number." << endl;
    }

*/


    // 3:

/*    int num1, num2;
    cout << "Enter the first number: ";
    cin >> num1;

    cout << "Enter the second number: ";
    cin >> num2;

    int max = (num1 > num2) ? num1 : num2;
    int lcm = max;

    while (true) {
        if (lcm % num1 == 0 && lcm % num2 == 0) {
            cout << "The LCM between " << num1 << " and " << num2 << " is: " << lcm << endl;
            break;
        }
        lcm += max;
    }

*/



    // 4:

/*    int number;
    int fa = 1;

    cout << "enter the number: ";
    cin >> number;

    for (int i = 1; i <= number; i++) {
        fa*=i;
    }
    cout << "factorial of " << number << " is: " << fa << endl;
*/


    // 5:

/*    int num;

    cout << "enter the number: ";
    cin >> num;

    if (num % 2 == 0)
        cout << num << " is a even number." << endl;
    else
        cout << num << " is a odd number." << endl;

*/



    // 6:

/*    int number;

    cout << "enter the number: ";
    cin >> number;

    int sum = 0;

    for (int i = 1; i <= number / 2; i++) {
        if (number % i == 0) {
            sum += i;
        }
    }
*/



    // 7:

/*    int num1, num2, num3;
    bool checker;

    cout << "enter smallest number: ";
    cin >> num1;

    cout << "enter the second number: ";
    cin >> num2;

    cout << "enter the biggest number: ";
    cin >> num3;

    if ( (num1*num1) + (num2*num2) == (num3*num3) ) {
        checker = true;
    }
    else
        checker = false;

    if (checker == true)
        cout << "pythagorean numbers" << endl;
    else
        cout << "not pythagorean numbers" << endl;

*/


    // 8:

/*    float discount, price, precentageD;

    cout << "enter price of product: ";
    cin >> price;

    cout << "enter precent of discount: ";
    cin >> precentageD;

    discount = (price * precentageD) / 100;

    cout << "final price: " << price-discount << endl;

*/


    // 9:

 /*  int n1, n2, gcd;

    cout << "first number: ";
    cin >> n1;

    cout << "second number: ";
    cin >> n2;

    int min = (n1 < n2) ? n1 : n2;

    for (int i = 1; i < min + 1; i++) {
        if (n1 % i == 0 && n2 % i == 0) {
            gcd = i;
        }
    }

    cout << "gcd of " << n1 << " and " << n2 << " is: " << gcd << endl;
*/

    return 0; // program finished successfully.

}
