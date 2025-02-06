#include <iostream>
using namespace std;

int convertBinary(int num) {
  int ans =0, pow = 1;

  while (num>0)
  {
    int reminder = num %2;
    num = num/2;

    ans = ans + (reminder * pow);
    pow = pow *10;
  }
  
  return ans;
}


int main() {
    int binary = convertBinary(10);
    cout <<binary<<endl;
    return 0;
}