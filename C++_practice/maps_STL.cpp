#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <map>
using namespace std;

// 1  X Y : add marks Y to to student whose name is X
// 2 X : erase the marks of the student whose name is X
// 3 X : print the marks of the studnets whose name is X ( if there is no such name print zero)
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int numlines;
    cin>> numlines;
    cin.ignore(); // to ignore the new line after integer input
    
    map<string, int> m; // map to sotre student names and their marks
    
    for ( int i = 0; i <= numlines; ++i){
        string line;
        getline(cin, line);
        
        stringstream ss(line); // use stringstream to split the line into parts
        int code, val;
        string name;
        
        // check the format of the line
        if (ss >>code >> name){ 
            if ( code == 1){
                ss >> val; // get marks for code 1
                m[name] += val;
            } else if ( code == 2){
                m.erase(name); // erase the student from map
            } else if ( code == 3){
                if (m.find(name) != m.end()){
                    cout << m[name] << endl;
                } else {
                    cout << "0" << endl;
                }
            }
            
        }
        
    }
    
    return 0;
}


  // input
  // 7
  // 1 Jesse 20
  // 1 Jess 12
  // 1 Jess 18
  // 3 Jess
  // 3 Jesse
  // 2 Jess
  // 3 Jess

  // output:
  // 30
  // 20
  // 0
