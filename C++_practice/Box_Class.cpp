#include<bits/stdc++.h>

using namespace std;
//Implement the class Box  
//l,b,h are integers representing the dimensions of the box

// The class should have the following functions : 

// Constructors: 
// Box();
// Box(int,int,int);
// Box(Box);


// int getLength(); // Return box's length
// int getBreadth (); // Return box's breadth
// int getHeight ();  //Return box's height
// long long CalculateVolume(); // Return the volume of the box

//Overload operator < as specified
//bool operator<(Box& b)

//Overload operator << as specified
//ostream& operator<<(ostream& out, Box& B)

class Box{
    private:
        int l,b,h;
        
    public:
        // constructors
        Box() : l(0), b(0), h(0){}
        // init l,b,h to 0
        // failed 3 cases when i didn't init to 0 and left it blank

        
        Box(int length, int breadth, int height) : l(length), b(breadth), h(height){
            // init l,b,h to given values
        }
        Box(const Box &B) : l(B.l), b(B.b), h(B.h){
            // copy dimension from variable to prober one like l = B.l
        }
        
        // functions to get the 3 variables
        int getLength(){
            return l;
        }
        int getBreadth(){
            return b;
        }
        int getHeight(){
            return h;
        }
        
        // function to calculate volume
        long long CalculateVolume(){
            return (long long) l * b * h; // calculate volume and make sure its long long for accuracy
        }
        
        // compare boxes
        bool operator<(Box &B){
            if ( l < B.l){
                return true;
            } else if (l == B.l && b < B.b) {
                return true;
            } else if (l == B.l && b == B.b && h < B.h) {
                return true;
            } else {
                return false;
            }
        }
        
        //Overload operator << as specified this one
        friend ostream& operator<<(ostream &out, Box &B){
            out << B.l << " " << B.b << " " << B.h; // format should be l b h
            return out;
        }

        
    
    
      
};

void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl;
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl;
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;
		}

	}
}

int main()
{
	check2();
}
