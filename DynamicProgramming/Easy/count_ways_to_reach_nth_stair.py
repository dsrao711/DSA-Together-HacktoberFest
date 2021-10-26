#https://practice.geeksforgeeks.org/problems/count-ways-to-nth-stairorder-does-not-matter5639/1/?category[]=Dynamic%20Programming&category[]=Dynamic%20Programming&company[]=Accolite&company[]=Morgan%20Stanley&company[]=BrowserStack&company[]=Accolite&company[]=Morgan%20Stanley&company[]=BrowserStack&page=1&query=category[]Dynamic%20Programmingcompany[]Accolitecompany[]Morgan%20Stanleycompany[]BrowserStackpage1company[]Accolitecompany[]Morgan%20Stanleycompany[]BrowserStackcategory[]Dynamic%20Programming#

# Math approach

class Solution:
    def nthStair(self,n):
        # Code here
        return 1 + n//2



if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        n = int(input())
        ob = Solution();
        ans = ob.nthStair(n)
        print(ans)