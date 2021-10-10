#include <iostream>
#include <string>
#include <ctype.h>
using namespace std;

//Function to Check Palindrome
bool Palindrome(string s)
{
  int i,j;
  i=0;
  j=s.length()-1;

  while(i<j)
  {
       //removing spaces and special characters
    while(i<j && isalnum(s[i])==0)
      i++;
    while(i<j && isalnum(s[j])==0)
      j--;

   //Checking if not palindrome
   if(toupper(s[i])!=toupper(s[j]))
    {
     return false;
    }
   else
   {
    i++;
    j--;
   }

  }
  return true;
}

//Main Function
int main() {

  string s;
  getline(cin,s);
  
  int ans=Palindrome(s);

  if(ans==1)
   cout<<"YES\n";
  else
   cout<<"NO\n";

 return 0;
}