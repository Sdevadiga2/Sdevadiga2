#include<iostream>
using namespace std;

class demo {
public:
    demo() {
        cout << "Constructor called: Object created" << endl;
    }
    ~demo() {
        cout << "Destructor called: Object destroyed" << endl;
    }
};

int main() {
    demo obj;
    return 0;
}
