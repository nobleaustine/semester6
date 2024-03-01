#include <iostream>
#include <thread>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <numeric> 
#include <chrono> 

using namespace std;
using namespace std::chrono;

void generate_sum(int size, long long& sum) {
    sum = 0;
    int* A = new int[size];
    for(int i = 0; i < size; i++){
        A[i] = rand();
    }
    for(int i = 0; i < size; i++) {
        sum += A[i];
    }
    delete[] A;
}

void do_parallel(int n,int t){

    vector<thread> threads;
    long long* sums = new long ;

    auto startTime = high_resolution_clock::now();

    for (int i = 0; i<t; i++){
        threads.push_back(thread(generate_sum, size, ref(sums[i])));
        }
    
    
    for (auto& th : threads) {
        th.join();
    }

    long long finalSum = accumulate(sums.begin(), sums.end(), 0LL);

    auto endTime = high_resolution_clock::now();

    auto duration = duration_cast<milliseconds>(endTime - startTime);
    cout << "Time taken: " << duration.count() << " milliseconds" << endl;

    cout << "Final sum: " << finalSum << endl;

}



int main() {
    int n, t; 
    cout << " " <<endl;
    cout << "sum of n random numbers using t threads"<<endl;
    cout << " " <<endl;
    cout << "Enter the size of the array: ";
    cin >> n;
    cout << "Enter the number of threads: ";
    cin >> t;
    srand(time(0));
   
    int size = n / t;

    


    return 0;
}
