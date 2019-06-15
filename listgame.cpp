#include <iostream>
using namespace std;

int main() {

    unsigned int in;
    cin >> in;

    unsigned int score = 0;
    unsigned int factor = 2;

    while (factor * factor <= in) {
        if (in % factor == 0) {
            score++;
            in /= factor;
        } else
            factor++;
    }

    cout << score + 1;

    return 0;
}