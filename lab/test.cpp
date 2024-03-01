// test cpp code snippets

#include <iostream>
#include <thread>

// Function to be executed in the thread
void sumArray(int arr[], int size) {
    int sum = 0;
    for (int i = 0; i < size; ++i) {
        sum += arr[i];
    }
    std::cout << "Sum of array elements: " << sum << std::endl;
}

int main() {
    constexpr int n = 5; // Size of the array
    int arr[n] = {1, 2, 3, 4, 5};

    // Create a thread and pass the array along with its size
    std::thread t(sumArray, arr, n);

    // Join the thread with the main thread
    t.join();

    return 0;
}
