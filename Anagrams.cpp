#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
    string s1,s2;
    cin>>s1>>s2;  int flag=0;
    int n1=s1.length();
    int n2= s2.length();

    if(n1==n2){
        sort(s1.begin(),s1.end());
        sort(s2.begin(),s2.end());
    }

    for(int i=0;i<n1;i++){
        if(s1[i]==s2[i]){
           flag=1;
        }
       else{
           flag=0;
       }
    }

    if(flag==1){
        cout<<"anagrams";
    }
    else{
        cout<<"NOt anagrams";
    }

    return 0;
}