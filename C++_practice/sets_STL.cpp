#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
#include <sstream>
using namespace std;

// 1 add element to set
// 2 delete an element from set
// 3 check if an element is in the set print Yes or No 


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int lines;
    set<int> st;
    cin >> lines;
    cin.ignore();
    
    for( int i =0; i < lines+1;++i){
        string line;
        getline(cin, line);
        
        stringstream ss(line);
        int a, b;
        
        if (ss >> a >> b){ // this fixed last 3 testcases needed to check if there is valid input
        if (a == 1){ // check if they want to add element
            st.insert(b);
        } else if ( a == 2){ // check if they want to delete a value form set
            st.erase(b);
        } else if ( a == 3){ // check if they want to check if value in set or not
            if (st.find(b) != st.end()){
                cout << "Yes" << "\n";
            } else {
                cout << "No" << "\n";
            }
        } else {
            cout << "Invalid input" << endl;
        }
        
        
      }
    }
    
    return 0;
}



