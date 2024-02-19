#include <iostream>
#include <thread>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <numeric> 
#include <chrono> 

using namespace std;
using namespace std::chrono;


void sum(int* A, int start, int end, long long& sum) {
    sum = 0;
    for (int i = start; i < end; i++) {
        sum += A[i];
    }
}

void do_parallel(int size, int ths){

    int* arr = new int[size];
   
    for (int i = 0; i < size; ++i) {
        arr[i] = rand();
    }

    int partitionSize = size / ths;
    vector<thread> threads;
    vector<long long> sums(ths);

   
    auto startTime = high_resolution_clock::now();

    
    for (int i = 0; i < ths; ++i) {
        int start = i * partitionSize;
        int end = (i == ths - 1) ? size : (i + 1) * partitionSize;
        threads.push_back(thread(sum, arr, start, end, ref(sums[i])));
    }

    for (auto& th : threads) {
        th.join();
    }


    long long finalSum = accumulate(sums.begin(), sums.end(), 0LL);


    auto endTime = high_resolution_clock::now();

    
    auto duration = duration_cast<microseconds>(endTime - startTime);

    cout<< "Array size: "<<size <<" "<<"Number of threads: "<<ths<<endl;
    cout << "Time taken: " << duration.count() << " microseconds" << endl;
    cout << "Sum: " << finalSum << endl;
    cout << " "<<endl;

    delete[] arr;


}



int main() {
    // int n, t; 
    // cout << " " <<endl;
    // cout << "sum of n random numbers using t threads"<<endl;
    // cout << " " <<endl;
    // cout << "Enter the size of the array: ";
    // cin >> n;
    // cout << "Enter the number of threads: ";
    // cin >> t;
    srand(time(0));
    do_parallel(1000,1);
    do_parallel(1000,2);
    do_parallel(1000,3);
    do_parallel(1000,4);
    do_parallel(1000,5);

    return 0;
}
