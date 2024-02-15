#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <thread>
#include <numeric>
#include <chrono>

void generateRandomArray(std::vector<int>& arr, int size) {

    std::srand(static_cast<unsigned int>(std::time(nullptr)));


    for (int i = 0; i < size; ++i) {
        arr.push_back(std::rand() % 100);  // Random integers between 0 and 99
    }
}

int sumSequential(const std::vector<int>& arr) {
    return std::accumulate(arr.begin(), arr.end(), 0);
}

int sumParallel(const std::vector<int>& arr, int numThreads) {
    int size = arr.size();
    int chunkSize = size / numThreads;

    std::vector<std::thread> threads;
    std::vector<int> partialSums(numThreads, 0);

    // Create threads and calculate partial sums
    // Inside sumParallel function
    for (int i = 0; i < numThreads; ++i) {
    threads.emplace_back([i, &arr, &partialSums, chunkSize, numThreads]() {
        int start = i * chunkSize;
        int end = (i == numThreads - 1) ? arr.size() : (i + 1) * chunkSize;
        partialSums[i] = std::accumulate(arr.begin() + start, arr.begin() + end, 0);
    });
}


    // Join threads
    for (auto& thread : threads) {
        thread.join();
    }

    // Calculate the total sum from partial sums
    return std::accumulate(partialSums.begin(), partialSums.end(), 0);
}

int main() {
    const int size = 1000000;  // Size of the random array
    const int numThreads = 4;  // Number of threads for parallel sum

    // Generate random array
    std::vector<int> randomArray;
    generateRandomArray(randomArray, size);

    // Calculate sum sequentially
    auto startSeq = std::chrono::high_resolution_clock::now();
    int sumSeq = sumSequential(randomArray);
    auto endSeq = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> durationSeq = endSeq - startSeq;

    // Calculate sum in parallel
    auto startParallel = std::chrono::high_resolution_clock::now();
    int sumParallelResult = sumParallel(randomArray, numThreads);
    auto endParallel = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> durationParallel = endParallel - startParallel;

    // Print results
    std::cout << "Sequential Sum: " << sumSeq << "\n";
    std::cout << "Parallel Sum: " << sumParallelResult << "\n";
    std::cout << "Sequential Execution Time: " << durationSeq.count() << " seconds\n";
    std::cout << "Parallel Execution Time: " << durationParallel.count() << " seconds\n";

    return 0;
}
