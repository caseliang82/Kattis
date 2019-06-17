#include <iostream>
#include <string>

using namespace std;

int main() {
    string convert[] {"@", "8", "(", "|)", "3", "#", "6", "[-]", "|", "_|", "|<", "1", R"([]\/[])", 
    "[]\\[]", "0", "|D", "(,)", "|Z", "$", "\'][\'", "|_|", R"(\/)", R"(\/\/)", "}{", R"(`/)", "2"};
    
    //cout << sizeof(convert)/sizeof(convert[0]) << endl;

    string in, out;
    getline(cin, in);

    for (int i = 0; i < in.length(); i++) {
        if (in[i] >= 'A' && in[i] <= 'Z') {
            out += convert[(int)in[i] - 65];
        } else if (in[i] >= 'a' && in[i] <= 'z') {
            out += convert[(int)in[i] - 97];
        } else {
            out += in[i];
        };

    }
    
    cout << out;

    return 0;
}
/*
What's the Frequency, Kenneth?

\/\/[-]@'][''$ ']['[-]3 #|Z3(,)|_|3[][](`/, |<3[][][][]3']['[-]?
\/\/[-]@'][''$ ']['[-]3 #|Z3(,)|_|3[]\[](`/, |<3[]\[][]\[]3']['[-]?
*/

