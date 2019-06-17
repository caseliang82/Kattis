#include<iostream>
#include<string>
using namespace std;

int main() {
    int n;
    scanf("%d", &n);
    while (n--) {
        string s;
        cin >> s;
        printf("%d\n", s.length());
    }

    return 0;
}