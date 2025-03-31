#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    string line;
    ifstream f ("2025/00/pub");

    getline(f, line);
    cout << line << endl;

    f.close();

    return 0;
}