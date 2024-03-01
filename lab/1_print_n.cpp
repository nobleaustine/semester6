#include <iostream>
#include <thread>
using namespace std;

void print(int n) {
    for (int i = 1; i <= n; i++) {
        cout<<i<<" ";
    }
    cout<<" "<<endl;
}

int main() {

    int n;
    cout << " " <<endl;
    cout << "Printing first n natural numbers in a thread"<<endl;
    cout << " " <<endl;

    cout << "Enter the value of n: ";
    cin >> n;
    cout << " " <<endl;
 
    cout << "First n natural numbers: ";
    thread t(print, n);
   
    t.join();
    
    cout << " " <<endl;
    return 0;

}
