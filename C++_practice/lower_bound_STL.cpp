#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    
    int n;
    cin >> n; // get number of numbers to store into vector
    vector<int> arr; // vector to store numbers
    
    for ( int i = 0; i < n; i++){
        int tmp;
        cin >> tmp;
        arr.push_back(tmp);
    }
    sort(arr.begin(), arr.end()); // make sure to sort the array before using lower_bound()
  
    int q;
    cin >> q; // get number of queries
    // put them into the vector
    vector<int> queries;
    for ( int i = 0; i < q;i++){
        int tmp;
        cin >> tmp;
        queries.push_back(tmp);
    }
    // run the quries
    for( int num : queries) {
      // Find the first position where num could be inserted without breaking the order
        auto low = lower_bound(arr.begin(), arr.end(), num);
        
        if ( low != arr.end() && *low == num) {
          // Found the number, output "Yes" and the 1-based index
            cout << "Yes " << (low - arr.begin()+1) << endl;
        } else {
          // Number not found, output "No" and the 1-based index of insertion
            cout << "No " << (low - arr.begin()+1) << endl;
        }
    }
    
    return 0;
}


// input:
// 8
//  1 1 2 2 6 9 9 15
//  4
//  1
//  4
//  9
//  15

// output:
// Yes 1
//  No 5
//  Yes 6
//  Yes 8
