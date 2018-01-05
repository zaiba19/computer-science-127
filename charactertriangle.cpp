//Name: Zaiba Iqbal
//This program asks user for a number and draws a triangle 
#include <iostream>
using namespace std;

int main()
{
int num;
cout<<"Enter a number:";
cin>>num;
 for (int i = 1; i <= num; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << endl;
    };
 return 0;
}