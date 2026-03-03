#include<iostream>
using namespace std;

int main()
{
    int *ptr = new int[10]();  // initialize to 0
    cout << "value: " << *ptr << endl;
    delete[] ptr;             // correct delete
    return 0;
}
