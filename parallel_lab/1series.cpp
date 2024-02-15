#include <iostream>
#include <thread>

void print_n_N(int n) {
    for (int i = 1; i <= n; ++i) {
        std::cout << i << " ";
    }
    std::cout << std::endl;
}

int main() {

    int n;
    
    // function name
    std::cout << " " <<std::endl;
    std::cout << "Printing first n natural numbers in a thread"<<std::endl;
    std::cout << " " <<std::endl;

    // Get the value of n from the user
    std::cout << "Enter the value of n: ";
    std::cin >> n;
    std::cout << " " <<std::endl;

    // Create a thread and pass the function along with its arguments
    std::cout << "First n natural numbers: ";
    std::thread t(print_n_N, n);
   
    // Wait for the created thread to finish
    t.join();
    
    std::cout << " " <<std::endl;
    return 0;

}
