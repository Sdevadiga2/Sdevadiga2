#include<iostream>
using namespace std;

class person {
protected:
    string name;
    int age;
public:
    person(string n, int a) {
        name = n;
        age = a;
    }
    void display() {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
    }
};

class student : public person {
private:
    char grade;
public:
    student(string n, int a, char g) : person(n, a) {
        grade = g;
    }

    void display() {
        person::display();
        cout << "Grade: " << grade << endl;
    }
};

int main() {
    student s("Anup", 21, 'A');
    s.display();
    return 0;
}
