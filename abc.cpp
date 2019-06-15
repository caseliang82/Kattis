#include <iostream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

int main()
{
    int a,b,c;
    char aa,bb,cc;
    cin >> a >> b >> c >> aa >> bb >> cc;

    char output[4];
    if (a > c) {
        a ^= c;
        c ^= a;
        a ^= c;
    }
    if (b > c) {
        b ^= c;
        c ^= b;
        b ^= c;
    } 
    if (a > b) {
        a ^= b;
        b ^= a;
        a ^= b;
    }

    if (aa == 'A') cout << a << " ";
    else if (aa == 'B') cout << b << " ";
    else cout << c << " ";

    if (bb == 'A') cout << a << " ";
    else if (bb == 'B') cout << b << " ";
    else cout << c << " ";

    if (cc == 'A') cout << a << " ";
    else if (cc == 'B') cout << b << " ";
    else cout << c << " ";



    return 0;
}