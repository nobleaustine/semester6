#include <iostream>
#include <thread>
#include <cstdlib>
using namespace std;

void sum(int* a,int n) {
   
    int s = 0;
    for (int i=0; i<n; i++) {
      
      s = s + a[i];
        
    }

    cout<<"Sum of elements: "<<s<<endl;
     
    
}

int main()
 {
   int n;
   cout << " " <<endl;
   cout << "Sum of n random numbers in a thread"<<endl;
   cout << " " <<endl;
   cout << "Enter the size of array: ";
   cin >> n;
   const int size = n;
   int *b = new int[n];
   srand(time(0)); 
  
   
   for (int i = 0; i < n; i++){
      b[i] = rand();
   }
   
   cout<<"Random array: ";
   for (int i = 0; i < n; i++){
      cout << b[i]<<" ";
   }
   cout<<" "<<endl;
   thread t(sum, b, size);
   

   t.join();

   return 0;
 }
