void printSubsequences(string inp, string subs)
{
if (inp.length() == 0)
{
cout << subs << endl;
return;
}
char apd = inp.at(0);
string substr = inp.erase(0, 1);
printSubsequences(substr, subs + apd);
printSubsequences(substr, subs);
}
