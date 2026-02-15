#include<iostream>
using namespace std;
class shape{
public:
    virtual void draw()=0;
    void info(){
    cout<<"this is shape"<<endl;
    }
};
    class circle:public shape{
    public:
    void draw(){
    cout<<"drawing a circle"<<endl;
    }
};
class rectangle:public shape{
public:
    void draw(){
    cout<<"drawing rectangle"<<endl;
    }
};
int main(){
    circle c;
    rectangle r;
    c.draw();
    r.draw();
    return 0;
}
